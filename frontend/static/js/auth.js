//Check if user is authenticated by calling /api/me, if not redirect to login page if so return user name.
export async function checkAuth() {
  const API_BASE_URL = window.location.origin;
  const response = await fetch(`${API_BASE_URL}/api/me`, {
    credentials: "include" //Include cookies for authentication
  });
  if (!response.ok) {
    window.location.href = `${API_BASE_URL}/index`;//redirect to login if not authenticated
    return null;
}const user = await response.json();
return user;
}