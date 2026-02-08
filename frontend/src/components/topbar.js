export function renderTopbar(email = "unknown") {
  return `
    <div class="topbar">
      <div>
        <p class="muted" style="font-size:14px;">Logged in as</p>
        <strong id="userEmail">${email}</strong>
      </div>
      <button id="logoutBtn" class="btn btn-danger">Logout</button>
    </div>
  `;
}
