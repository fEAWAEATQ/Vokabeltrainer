export function logout() {
const API_BASE_URL = window.location.origin;
const logoutform = document.getElementById("logout-form"); //Logout-Formular
if (logoutform) {
  logoutform.addEventListener("submit", async (e) => {
    e.preventDefault();
    const response = await fetch(`${API_BASE_URL}/api/auth/logout`, {
      method: "POST",
      headers: { "Content-Type": "application/json" }
    });
    if (response.ok) {
      window.location.href = `${API_BASE_URL}/index`;//redirect to login after logout
    } else {
      alert("Logout failed");
    }
  });
}
}