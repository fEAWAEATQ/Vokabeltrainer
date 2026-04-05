export function nav() {
  const API_BASE_URL = window.location.origin;
const dashboardBtn = document.getElementById("dashboard-btn"); //Navigation buttons in dashboard.html
if (dashboardBtn) {
  dashboardBtn.addEventListener("click", () => {
    window.location.href = `${API_BASE_URL}/dashboard`;
  });
}
const statsBtn = document.getElementById("stats-btn");//Navigation buttons in dashboard.html
if (statsBtn) {
  statsBtn.addEventListener("click", () => {
    window.location.href = `${API_BASE_URL}/stats`;
  });
}
const practiceBtn = document.getElementById("practice-btn");//Navigation buttons in dashboard.html
if (practiceBtn) { 
   practiceBtn.addEventListener("click", () => {
    window.location.href = `${API_BASE_URL}/practice`;
  });
}
}