//Check if user is authenticated by calling /api/me, if not redirect to login page if so return user name.
async function checkAuth() {
  const API_BASE_URL = window.location.origin;
  const response = await fetch(`${API_BASE_URL}/api/me`, {
    credentials: "include" //Include cookies for authentication
  });
  if (!response.ok) {
    window.location.href = `${API_BASE_URL}/index.html`;//redirect to login if not authenticated
    return null;
}const user = await response.json();
return user;
}

document.addEventListener("DOMContentLoaded", async () => {
  console.log("App.js loaded");
  const API_BASE_URL = window.location.origin;
 const usernamePlaceholder = document.getElementById("username-placeholder"); //Element in dashboard.html to display username and check if user is authenticated
if (usernamePlaceholder) {
  const user = await checkAuth();
  if (!user) return;
  usernamePlaceholder.textContent = user.username;
}

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
  body: JSON.stringify({ username, password }),
  credentials: "include" //Include cookies for authentication
});
if (response.ok) {
  window.location.href = `${API_BASE_URL}/dashboard.html`;//redirect to dashboard after successful registration
} else {
  alert("Registration failed");
  }
 });
}

const logoutform = document.getElementById("logout-form"); //Logout-Formular
if (logoutform) {
  logoutform.addEventListener("submit", async (e) => {
    e.preventDefault();
    const response = await fetch(`${API_BASE_URL}/api/auth/logout`, {
      method: "POST",
      headers: { "Content-Type": "application/json" }
    });
    if (response.ok) {
      window.location.href = `${API_BASE_URL}/index.html`;//redirect to login after logout
    } else {
      alert("Logout failed");
    }
  });
}

const dashboardBtn = document.getElementById("dashboard-btn"); //Navigation buttons in dashboard.html
if (dashboardBtn) {
  dashboardBtn.addEventListener("click", () => {
    window.location.href = `${API_BASE_URL}/dashboard.html`;
  });
}
const statsBtn = document.getElementById("stats-btn");
if (statsBtn) {
  statsBtn.addEventListener("click", () => {
    window.location.href = `${API_BASE_URL}/stats.html`;
  });
}
const practiceBtn = document.getElementById("practice-btn");
if (practiceBtn) { 
   practiceBtn.addEventListener("click", () => {
    window.location.href = `${API_BASE_URL}/practice.html`;
  });
}
});




