export function renderTopbar(email = "unknown") {
  const initial = (email?.trim()?.[0] || "U").toUpperCase();

  return `
    <div class="topbar">
      <div>
        <p class="muted" style="font-size:14px;">Logged in as</p>
        <strong id="userEmail">${email}</strong>
      </div>

      <div style="display:flex; align-items:center; gap:12px; position:relative;">
        <!-- Avatar -->
        <div
          id="avatarBtn"
          style="
            width:42px;
            height:42px;
            border-radius:999px;
            display:flex;
            align-items:center;
            justify-content:center;
            font-weight:900;
            background: linear-gradient(90deg, #0ea5e9, #6366f1, #a855f7);
            color:white;
            cursor:pointer;
            user-select:none;
          "
          title="Account"
        >
          ${initial}
        </div>

        <!-- Dropdown -->
        <div
          id="profileMenu"
          style="
            position:absolute;
            top:52px;
            right:0;
            width:280px;
            background:white;
            border:1px solid var(--border);
            border-radius:16px;
            box-shadow:0 20px 60px rgba(0,0,0,0.15);
            padding:12px;
            display:none;
            z-index:999;
          "
        >
          <div
  style="
    font-weight:900;
    font-size:14px;
    max-width:100%;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
  "
  title="${email}"
>
  ${email}
</div>

          <div class="muted" style="margin-top:4px; font-size:13px;">
            Job Search Agent User
          </div>

          <div style="height:1px; background:var(--border); margin:12px 0;"></div>

          <button class="btn btn-danger" id="logoutBtn" style="width:100%;">
            Logout
          </button>
        </div>
      </div>
    </div>
  `;
}
