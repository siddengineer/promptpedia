const state = { q: "", category: "", framework: "", page: 1, pageSize: 24, totalPages: 1 };

let PROMPTS = [];

const els = {
  cardGrid: document.getElementById("cardGrid"),
  resultsLabel: document.getElementById("resultsLabel"),
  breadcrumb: document.getElementById("breadcrumb"),
  pager: document.getElementById("pager"),
  emptyState: document.getElementById("emptyState"),
  searchInput: document.getElementById("searchInput"),
  clearSearch: document.getElementById("clearSearch"),
  drawerList: document.getElementById("drawerList"),
  allDrawer: document.getElementById("allDrawer"),
  frameworkChips: document.getElementById("frameworkChips"),
  shuffleBtn: document.getElementById("shuffleBtn"),
  contributeBtn: document.getElementById("contributeBtn"),
  statTotal: document.getElementById("statTotal"),
  statCats: document.getElementById("statCats"),
  statFrameworks: document.getElementById("statFrameworks"),
  overlay: document.getElementById("cardOverlay"),
  overlayContent: document.getElementById("cardFullContent"),
  overlayClose: document.getElementById("overlayClose"),
  toast: document.getElementById("toast"),
};

let debounceTimer = null;
const CONTRIBUTE_EMAIL = "bigdog202224@gmail.com";

async function init() {
  try {
    const res = await fetch("./data/prompts.json");
    if (!res.ok) throw new Error("Failed to load prompts.json");
    PROMPTS = await res.json();
  } catch (err) {
    els.resultsLabel.textContent = "Couldn't load the catalog. Check that data/prompts.json is next to index.html.";
    console.error(err);
    return;
  }

  const categories = [...new Set(PROMPTS.map((p) => p.category))].sort();
  const frameworks = [...new Set(PROMPTS.map((p) => p.framework))].sort();
  const counts = {};
  PROMPTS.forEach((p) => (counts[p.category] = (counts[p.category] || 0) + 1));

  els.statTotal.textContent = PROMPTS.length;
  els.statCats.textContent = categories.length;
  els.statFrameworks.textContent = frameworks.length;

  renderDrawers(counts, categories);
  renderFrameworkChips(frameworks);
  bindEvents();
  loadPrompts();
}

function renderDrawers(counts, categories) {
  els.drawerList.innerHTML = "";
  categories.forEach((cat, i) => {
    const btn = document.createElement("button");
    btn.className = "drawer-btn";
    btn.dataset.category = cat;
    btn.innerHTML = `
      <span class="drawer-tab-num">${String(i + 1).padStart(2, "0")}</span>
      <span class="drawer-tab-name">${cat}</span>
      <span class="drawer-count">${counts[cat]}</span>
    `;
    btn.addEventListener("click", () => selectCategory(cat, btn));
    els.drawerList.appendChild(btn);
  });
}

function renderFrameworkChips(frameworks) {
  els.frameworkChips.innerHTML = "";
  frameworks.forEach((fw) => {
    const chip = document.createElement("button");
    chip.className = "fw-chip";
    chip.textContent = fw;
    chip.dataset.framework = fw;
    chip.addEventListener("click", () => selectFramework(fw, chip));
    els.frameworkChips.appendChild(chip);
  });
}

function selectCategory(cat, btn) {
  state.category = state.category === cat ? "" : cat;
  state.page = 1;
  document.querySelectorAll(".drawer-btn").forEach((b) => b.classList.remove("active"));
  if (state.category) btn.classList.add("active");
  else els.allDrawer.classList.add("active");
  loadPrompts();
}

function selectFramework(fw, chip) {
  state.framework = state.framework === fw ? "" : fw;
  state.page = 1;
  document.querySelectorAll(".fw-chip").forEach((c) => c.classList.remove("active"));
  if (state.framework) chip.classList.add("active");
  loadPrompts();
}

function bindEvents() {
  els.allDrawer.addEventListener("click", () => {
    state.category = "";
    state.page = 1;
    document.querySelectorAll(".drawer-btn").forEach((b) => b.classList.remove("active"));
    els.allDrawer.classList.add("active");
    loadPrompts();
  });

  els.searchInput.addEventListener("input", (e) => {
    state.q = e.target.value;
    els.clearSearch.hidden = !state.q;
    state.page = 1;
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(loadPrompts, 200);
  });

  els.clearSearch.addEventListener("click", () => {
    els.searchInput.value = "";
    state.q = "";
    els.clearSearch.hidden = true;
    state.page = 1;
    loadPrompts();
  });

  els.shuffleBtn.addEventListener("click", () => {
    const card = PROMPTS[Math.floor(Math.random() * PROMPTS.length)];
    openCard(card);
  });

  els.overlayClose.addEventListener("click", closeOverlay);
  els.overlay.addEventListener("click", (e) => {
    if (e.target === els.overlay) closeOverlay();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeOverlay();
  });

  els.contributeBtn.addEventListener("click", openContributeForm);
}

function closeOverlay() {
  els.overlay.hidden = true;
  els.overlay.style.display = "none";
}

function loadPrompts() {
  let results = PROMPTS;
  if (state.category) results = results.filter((p) => p.category === state.category);
  if (state.framework) results = results.filter((p) => p.framework === state.framework);
  if (state.q) {
    const needle = state.q.trim().toLowerCase();
    results = results.filter(
      (p) =>
        p.title.toLowerCase().includes(needle) ||
        p.prompt.toLowerCase().includes(needle) ||
        p.category.toLowerCase().includes(needle)
    );
  }

  const total = results.length;
  state.totalPages = Math.max(1, Math.ceil(total / state.pageSize));
  if (state.page > state.totalPages) state.page = state.totalPages;
  const start = (state.page - 1) * state.pageSize;
  const pageItems = results.slice(start, start + state.pageSize);

  renderResultsLabel(total);
  renderGrid(pageItems);
  renderPager();
}

function renderResultsLabel(total) {
  const parts = [];
  if (state.category) parts.push(state.category);
  if (state.framework) parts.push(state.framework);
  els.breadcrumb.textContent = parts.join(" · ");
  els.resultsLabel.textContent = `${total} card${total === 1 ? "" : "s"} filed`;
}

function renderGrid(results) {
  els.cardGrid.innerHTML = "";
  els.emptyState.hidden = results.length !== 0;
  results.forEach((p) => {
    const card = document.createElement("article");
    card.className = "prompt-card";
    card.tabIndex = 0;
    card.innerHTML = `
      <div class="card-row-top">
        <span class="card-id">No. ${String(p.id).padStart(3, "0")}</span>
        <span class="card-framework">${p.framework}</span>
      </div>
      <h3 class="card-title">${escapeHTML(p.title)}</h3>
      <div class="card-category">${escapeHTML(p.category)}</div>
      <p class="card-snippet">${escapeHTML(p.prompt)}</p>
      <div class="card-footer">
        <span class="card-cta">Read card →</span>
        <button class="copy-btn" data-id="${p.id}">Copy</button>
      </div>
    `;
    card.addEventListener("click", (e) => {
      if (e.target.classList.contains("copy-btn")) return;
      openCard(p);
    });
    card.addEventListener("keydown", (e) => {
      if (e.key === "Enter") openCard(p);
    });
    card.querySelector(".copy-btn").addEventListener("click", (e) => {
      e.stopPropagation();
      copyText(p.prompt);
    });
    els.cardGrid.appendChild(card);
  });
}

function renderPager() {
  els.pager.innerHTML = "";
  if (state.totalPages <= 1) return;

  const mk = (label, page, opts = {}) => {
    const b = document.createElement("button");
    b.textContent = label;
    if (opts.active) b.classList.add("active");
    if (opts.disabled) b.disabled = true;
    b.addEventListener("click", () => {
      state.page = page;
      loadPrompts();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    return b;
  };

  els.pager.appendChild(mk("‹ Prev", state.page - 1, { disabled: state.page <= 1 }));

  const total = state.totalPages;
  const cur = state.page;
  const pages = new Set([1, total, cur, cur - 1, cur + 1]);
  let prev = 0;
  [...pages]
    .filter((n) => n >= 1 && n <= total)
    .sort((a, b) => a - b)
    .forEach((n) => {
      if (prev && n - prev > 1) {
        const dots = document.createElement("span");
        dots.textContent = "…";
        dots.style.padding = "0 4px";
        dots.style.color = "var(--ink-soft)";
        els.pager.appendChild(dots);
      }
      els.pager.appendChild(mk(String(n), n, { active: n === cur }));
      prev = n;
    });

  els.pager.appendChild(mk("Next ›", state.page + 1, { disabled: state.page >= total }));
}

function openCard(p) {
  els.overlayContent.innerHTML = `
    <div class="full-id">Catalog No. ${String(p.id).padStart(3, "0")}</div>
    <h2 class="full-title">${escapeHTML(p.title)}</h2>
    <div class="full-meta">
      <span class="full-tag">${escapeHTML(p.category)}</span>
      <span class="full-tag">${escapeHTML(p.framework)} framework</span>
    </div>
    <div class="full-prompt">${escapeHTML(p.prompt)}</div>
    <div class="full-actions">
      <button id="fullCopyBtn">Copy prompt</button>
      <button class="secondary" id="fullCloseBtn">Close</button>
    </div>
  `;
  els.overlay.hidden = false;
  els.overlay.style.display = "flex";
  document.getElementById("fullCopyBtn").addEventListener("click", () => copyText(p.prompt));
  document.getElementById("fullCloseBtn").addEventListener("click", closeOverlay);
}

function openContributeForm() {
  const categories = [...new Set(PROMPTS.map((p) => p.category))].sort();
  const options = categories.map((c) => `<option value="${escapeHTML(c)}">${escapeHTML(c)}</option>`).join("");

  els.overlayContent.innerHTML = `
    <div class="full-id">New Submission Card</div>
    <h2 class="full-title">Contribute a Prompt</h2>
    <p class="contrib-hint">Fill this out and it opens your email app, pre-addressed to
      <a href="mailto:${CONTRIBUTE_EMAIL}">${CONTRIBUTE_EMAIL}</a> with your prompt ready to send.</p>

    <div class="contrib-field">
      <label for="contribTitle">Prompt title</label>
      <input type="text" id="contribTitle" placeholder="e.g. Weekly Content Calendar Builder" />
    </div>

    <div class="contrib-field">
      <label for="contribCategory">Category</label>
      <select id="contribCategory">
        ${options}
        <option value="Other / New category">Other / New category</option>
      </select>
    </div>

    <div class="contrib-field">
      <label for="contribFramework">Framework (optional)</label>
      <input type="text" id="contribFramework" placeholder="e.g. RTF, AIDA, STAR..." />
    </div>

    <div class="contrib-field">
      <label for="contribPrompt">Prompt text</label>
      <textarea id="contribPrompt" rows="6" placeholder="Write the full prompt here..."></textarea>
    </div>

    <div class="contrib-field">
      <label for="contribName">Your name or credit (optional)</label>
      <input type="text" id="contribName" placeholder="How should we credit you?" />
    </div>

    <div class="full-actions">
      <button id="contribGmailBtn">Open in Gmail</button>
      <button class="secondary" id="contribCopyBtn">Copy details</button>
      <button class="secondary" id="contribCloseBtn">Cancel</button>
    </div>
    <div class="contrib-note">
      Gmail not working for you? <a href="#" id="contribMailtoLink">Try your default email app instead</a>,
      or use Copy details and paste into any email to
      <a href="mailto:${CONTRIBUTE_EMAIL}">${CONTRIBUTE_EMAIL}</a>.
    </div>
    <div class="contrib-note">Card cabinet review before filing &mdash; not published automatically.</div>
  `;

  els.overlay.hidden = false;
  els.overlay.style.display = "flex";

  document.getElementById("contribCloseBtn").addEventListener("click", closeOverlay);
  document.getElementById("contribGmailBtn").addEventListener("click", () => submitContribution("gmail"));
  document.getElementById("contribCopyBtn").addEventListener("click", () => submitContribution("copy"));
  document.getElementById("contribMailtoLink").addEventListener("click", (e) => {
    e.preventDefault();
    submitContribution("mailto");
  });
}

function buildContributionPayload() {
  const title = document.getElementById("contribTitle").value.trim();
  const category = document.getElementById("contribCategory").value.trim();
  const framework = document.getElementById("contribFramework").value.trim();
  const promptText = document.getElementById("contribPrompt").value.trim();
  const name = document.getElementById("contribName").value.trim();

  if (!title || !promptText) {
    alert("Please add at least a title and the prompt text before sending.");
    return null;
  }

  const subject = `Promptpedia Submission: ${title}`;
  const bodyLines = [
    `Title: ${title}`,
    `Category: ${category || "(not specified)"}`,
    `Framework: ${framework || "(not specified)"}`,
    `Submitted by: ${name || "(anonymous)"}`,
    "",
    "Prompt:",
    promptText,
  ];
  return { subject, body: bodyLines.join("\n") };
}

function submitContribution(method) {
  const payload = buildContributionPayload();
  if (!payload) return;
  const { subject, body } = payload;

  if (method === "gmail") {
    const url = `https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=${encodeURIComponent(
      CONTRIBUTE_EMAIL
    )}&su=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    window.open(url, "_blank");
  } else if (method === "mailto") {
    window.location.href = `mailto:${CONTRIBUTE_EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  } else if (method === "copy") {
    copyText(`To: ${CONTRIBUTE_EMAIL}\nSubject: ${subject}\n\n${body}`);
  }
}

function copyText(text) {
  navigator.clipboard.writeText(text).then(showToast).catch(() => {
    const ta = document.createElement("textarea");
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand("copy");
    document.body.removeChild(ta);
    showToast();
  });
}

function showToast() {
  els.toast.hidden = false;
  els.toast.textContent = "Copied to clipboard";
  clearTimeout(showToast._t);
  showToast._t = setTimeout(() => (els.toast.hidden = true), 1800);
}

function escapeHTML(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

init();
