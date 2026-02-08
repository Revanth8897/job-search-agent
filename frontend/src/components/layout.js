import { renderSidebar } from "./sidebar.js";
import { renderTopbar } from "./topbar.js";
import { authStore } from "../context/authStore.js";
import { authApi } from "../api/authApi.js";

export function renderDashboardLayout({ active, content }) {
  const user = authStore.getUser();

  const app = document.getElementById("app");
  app.innerHTML = `
    <div class="dashboard">
      ${renderSidebar(active)}
      <div class="main">
        ${renderTopbar(user?.email || "unknown")}
        <div class="page">
          ${content}
        </div>
      </div>
    </div>
  `;

  const logoutBtn = document.getElementById("logoutBtn");
  logoutBtn.addEventListener("click", async () => {
    await authApi.logout();
    window.location.href = "./login.html";
  });
}
