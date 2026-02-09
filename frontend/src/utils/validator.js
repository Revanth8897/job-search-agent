export function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

export function minLength(str, len) {
  return (str || "").trim().length >= len;
}
