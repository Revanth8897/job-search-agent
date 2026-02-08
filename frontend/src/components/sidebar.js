export function renderSidebar(active = "home") {
  return `
    <aside class="sidebar">
      <h2>Job Agent</h2>
      <div class="nav">
        <a href="./dashboard.html" class="${active === "home" ? "active" : ""}">Home</a>
        <a href="./resume-upload.html" class="${active === "resume" ? "active" : ""}">Resume Upload</a>
        <a href="./skills.html" class="${active === "skills" ? "active" : ""}">Skills</a>
        <a href="./jobs.html" class="${active === "jobs" ? "active" : ""}">Jobs</a>
        <a href="./wireframes.html" class="${active === "wireframes" ? "active" : ""}">Wireframes</a>
      </div>
    </aside>
  `;
}

