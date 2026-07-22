# Promptpedia (Static Site)

A card-catalog styled library of 590 AI prompts across 18 fields. This is a
**pure static site** — plain HTML, CSS, and JS. No server, no backend, no
Python, no build step, no cost to run. It just needs to be hosted as files.

```
promptpedia-static/
├── index.html
├── style.css
├── script.js
└── data/
    └── prompts.json   # all 590 prompts
```

## Try it locally first

Just double-click `index.html`... actually don't — most browsers block
`fetch()` of local files opened via `file://`. Instead, run a tiny local
server for testing (any of these work, pick whichever you have installed):

```bash
# Python (built in on most systems)
cd promptpedia-static
python3 -m http.server 8000
# then open http://localhost:8000

# or Node
npx serve .
```

## Deploy for free (pick one — all are $0)

### 1. GitHub Pages (easiest if you already use GitHub)
1. Create a new GitHub repo and push the contents of this folder to it
   (the files should sit at the repo root, or in a `/docs` folder).
2. Go to the repo's **Settings → Pages**.
3. Under "Build and deployment", set Source to your branch (e.g. `main`)
   and folder (root or `/docs`).
4. Save. Your site will be live at `https://<username>.github.io/<repo>/`
   within a minute or two.

### 2. Netlify (drag-and-drop, no account setup needed for a quick test)
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop).
2. Drag the whole `promptpedia-static` folder onto the page.
3. Done — you get a live URL immediately. Create a free account to keep
   it permanently and get a custom subdomain like `promptpedia.netlify.app`.

### 3. Cloudflare Pages
1. Sign up at [pages.cloudflare.com](https://pages.cloudflare.com) (free tier).
2. "Create a project" → "Upload assets" (no Git needed) → upload this folder.
3. Deploy. You get a `*.pages.dev` URL, plus free custom domain support.

### 4. Vercel
1. Sign up at [vercel.com](https://vercel.com) (free tier).
2. "Add New Project" → import the folder or a connected Git repo.
3. Framework preset: "Other" (it's static, no build command needed).
4. Deploy — you get a `*.vercel.app` URL.

All four have generous free tiers that comfortably cover a project like this
(a handful of small static files, no database, no server-side compute).

## Updating the prompts later

Just edit `data/prompts.json` directly (it's a plain array of
`{id, category, title, framework, prompt}` objects), or regenerate it using
the `gen.py` script from the full project if you have it, then re-upload/
re-push to whichever host you chose. There's no database and no backend to
manage — the JSON file *is* the database.

## Notes

- The "Contribute a Prompt" button opens a pre-filled `mailto:` link to
  **bigdog202224@gmail.com** — no backend or form-handling service needed.
- All search/filter/pagination happens entirely in the browser after the
  one-time load of `data/prompts.json` (~220 KB), so it stays fast even
  on the free tiers of any host above.
