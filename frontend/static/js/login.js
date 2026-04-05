document.addEventListener("DOMContentLoaded", () => {
    const API_BASE_URL = window.location.origin;
const form = document.getElementById("login-form"); //Login-Formular in login.html
  if (form) {
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });
    if (response.ok) {
      window.location.href = `${API_BASE_URL}/dashboard`;
    } else {
      alert("Login failed");
    }
  });
}
  const registerButton = document.getElementById("register-button");//Register-Button in login.html
  if (registerButton) {
    registerButton.addEventListener("click", () => {
      window.location.href = `${API_BASE_URL}/register`;
    });
  }
});