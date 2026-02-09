import { authStore } from "../context/authStore.js";

export function requireAuth() {
  const user = authStore.getUser();
  if (!user) window.location.href = "./login.html";
}
