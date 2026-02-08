import { authStore } from "../context/authStore.js";

export function useAuth() {
  return {
    user: authStore.getUser(),
    token: authStore.getToken()
  };
}
