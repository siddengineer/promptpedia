import json
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "prompts.json"
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app = FastAPI(
    title="Promptpedia API",
    description="A searchable library of AI prompts across every field.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open(DATA_FILE, "r", encoding="utf-8") as f:
    PROMPTS = json.load(f)

CATEGORIES = sorted({p["category"] for p in PROMPTS})
FRAMEWORKS = sorted({p["framework"] for p in PROMPTS})


@app.get("/api/health")
def health():
    return {"status": "ok", "total_prompts": len(PROMPTS)}


@app.get("/api/stats")
def stats():
    counts = {}
    for p in PROMPTS:
        counts[p["category"]] = counts.get(p["category"], 0) + 1
    return {
        "total_prompts": len(PROMPTS),
        "total_categories": len(CATEGORIES),
        "total_frameworks": len(FRAMEWORKS),
        "per_category": counts,
    }


@app.get("/api/categories")
def get_categories():
    return {"categories": CATEGORIES}


@app.get("/api/frameworks")
def get_frameworks():
    return {"frameworks": FRAMEWORKS}


@app.get("/api/prompts")
def get_prompts(
    q: Optional[str] = Query(None, description="Search text across title and prompt"),
    category: Optional[str] = Query(None, description="Filter by exact category"),
    framework: Optional[str] = Query(None, description="Filter by exact framework"),
    page: int = Query(1, ge=1),
    page_size: int = Query(24, ge=1, le=100),
):
    results = PROMPTS

    if category:
        results = [p for p in results if p["category"].lower() == category.lower()]

    if framework:
        results = [p for p in results if p["framework"].lower() == framework.lower()]

    if q:
        needle = q.strip().lower()
        results = [
            p for p in results
            if needle in p["title"].lower()
            or needle in p["prompt"].lower()
            or needle in p["category"].lower()
        ]

    total = len(results)
    start = (page - 1) * page_size
    end = start + page_size
    page_items = results[start:end]

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": max(1, (total + page_size - 1) // page_size),
        "results": page_items,
    }


@app.get("/api/prompts/{prompt_id}")
def get_prompt(prompt_id: int):
    for p in PROMPTS:
        if p["id"] == prompt_id:
            return p
    raise HTTPException(status_code=404, detail="Prompt not found")


@app.get("/api/random")
def random_prompt():
    import random
    return random.choice(PROMPTS)


# ---- Serve the frontend ----
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/")
def serve_index():
    return FileResponse(FRONTEND_DIR / "index.html")
