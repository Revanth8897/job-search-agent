import { storage } from "../utils/storage.js";

const USER_KEY = "job_agent_user";
const TOKEN_KEY = "job_agent_token";
const REGISTERED_KEY = "job_agent_registered_user";

export const authStore = {
  // Logged-in user
  getUser() {
    return storage.get(USER_KEY);
  },

  setUser(user) {
    storage.set(USER_KEY, user);
  },

  setToken(token) {
    storage.set(TOKEN_KEY, token);
  },

  getToken() {
    return storage.get(TOKEN_KEY);
  },

  logout() {
    storage.remove(USER_KEY);
    storage.remove(TOKEN_KEY);
  },

  // Registered user (credentials storage for Week 1)
  getRegisteredUser() {
    return storage.get(REGISTERED_KEY);
  },

  setRegisteredUser(user) {
    storage.set(REGISTERED_KEY, user);
  }
};
