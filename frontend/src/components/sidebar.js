function getSavedCount() {
  try {
    const saved = JSON.parse(localStorage.getItem("saved_jobs")) || [];
    return saved.length;
  } catch {
    return 0;
  }
}

export function renderSidebar(active = "home") {
  const savedCount = getSavedCount();

  return `
    <aside class="sidebar">
      <h2>Job Agent</h2>

      <div class="nav">
        <a href="./dashboard.html" class="${active === "home" ? "active" : ""}">
          Home
        </a>

        <a href="./resume-upload.html" class="${active === "resume" ? "active" : ""}">
          Resume Upload
        </a>

        <a href="./skills.html" class="${active === "skills" ? "active" : ""}">
          Skills
        </a>

        <a href="./jobs.html" class="${active === "jobs" ? "active" : ""}">
          Jobs
        </a>

        <!-- WEEK 3 -->
        <a href="./recommendations.html" class="${active === "reco" ? "active" : ""}">
          Recommendations
        </a>

        <!-- WEEK 3 -->
        <a href="./tracking.html" class="${active === "tracking" ? "active" : ""}">
          Tracking
        </a>

        <a href="./saved-jobs.html" class="${active === "saved" ? "active" : ""}">
          Saved Jobs
          <span
            id="savedBadge"
            style="
              margin-left:auto;
              font-size:12px;
              font-weight:900;
              padding:4px 10px;
              border-radius:999px;
              background:rgba(99,102,241,0.12);
              border:1px solid rgba(99,102,241,0.25);
              color:#4f46e5;
              display:${savedCount > 0 ? "inline-flex" : "none"};
            "
          >
            ${savedCount}
          </span>
        </a>
      </div>
    </aside>
  `;
}

/* Called after sidebar is rendered */
export function initSidebarBadgeSync() {
  function updateBadge() {
    const badge = document.getElementById("savedBadge");
    if (!badge) return;

    const count = getSavedCount();
    badge.textContent = count;
    badge.style.display = count > 0 ? "inline-flex" : "none";
  }

  window.addEventListener("savedJobsUpdated", updateBadge);
  updateBadge();
}
