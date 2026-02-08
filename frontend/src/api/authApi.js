import { authStore } from "../context/authStore.js";

export const authApi = {
  async register({ name, email, password }) {
    // Save registered credentials
    const registeredUser = { name, email, password };
    authStore.setRegisteredUser(registeredUser);

    // IMPORTANT: Do NOT log user in here
    return { message: "Registered successfully" };
  },

  async login({ email, password }) {
    const reg = authStore.getRegisteredUser();

    if (!reg) {
      throw new Error("No account found. Please register first.");
    }

    if (reg.email !== email) {
      throw new Error("Email not found. Please register first.");
    }

    if (reg.password !== password) {
      throw new Error("Wrong password.");
    }

    // Login success
    const user = { name: reg.name, email: reg.email };
    authStore.setUser(user);
    authStore.setToken("mock-token");

    return { user, token: "mock-token" };
  },

  async logout() {
    authStore.logout();
  }
};
