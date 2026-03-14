document.addEventListener("DOMContentLoaded", () => {
  console.log("App.js loaded");

  const API_BASE_URL = window.location.origin;

  const form = document.getElementById("login-form"); //Login-Formular
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
      window.location.href = `${API_BASE_URL}/dashboard.html`;
    } else {
      alert("Login failed");
    }
  });
}
  const registerButton = document.getElementById("register-button");//Register-Button
  if (registerButton) {
    registerButton.addEventListener("click", () => {
      window.location.href = `${API_BASE_URL}/register.html`;
    });
  }
const backToLoginButton = document.getElementById("back-to-login");//Button in Register.html to go back to Login.html
if (backToLoginButton) {
  backToLoginButton.addEventListener("click", () => {
    window.location.href = `${API_BASE_URL}/index.html`;
  });
}
 const registerForm = document.getElementById("register-form"); //Register-Formular
 if (registerForm) {
  registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();
const username = document.getElementById("username").value;
const password = document.getElementById("password").value;
const response = await fetch(`${API_BASE_URL}/api/users`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ username, password })
});
if (response.ok) {
  window.location.href = `${API_BASE_URL}/dashboard.html`;//redirect to dashboard after successful registration
} else {
  alert("Registration failed");
  }
 });
}
});
