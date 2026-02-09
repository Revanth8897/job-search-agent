import { renderSidebar, initSidebarBadgeSync } from "./sidebar.js";
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
initSidebarBadgeSync();


  const logoutBtn = document.getElementById("logoutBtn");
  logoutBtn.addEventListener("click", async () => {
    await authApi.logout();
    window.location.href = "./login.html";
  });
  // Profile dropdown
const avatarBtn = document.getElementById("avatarBtn");
const profileMenu = document.getElementById("profileMenu");

avatarBtn.addEventListener("click", (e) => {
  e.stopPropagation();
  profileMenu.style.display =
    profileMenu.style.display === "block" ? "none" : "block";
});

document.addEventListener("click", () => {
  profileMenu.style.display = "none";
});

}
