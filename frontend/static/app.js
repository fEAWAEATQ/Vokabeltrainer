document.addEventListener("DOMContentLoaded", () => {
  console.log("App.js loaded");

  const API_BASE_URL = window.location.origin;

  const form = document.getElementById("login-form");
  if (!form) {
    console.error("login-form not found");
    return;
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (response.ok) {
      alert("Login successful");
    } else {
      alert("Login failed");
    }
  });
});
