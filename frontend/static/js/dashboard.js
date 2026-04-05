import { checkAuth } from "./auth.js"; 
import {nav} from "./nav.js";
import {logout} from "./logout.js";
document.addEventListener("DOMContentLoaded", async () => {
 const usernamePlaceholder = document.getElementById("username-placeholder"); //Element in dashboard.html to display username and check if user is authenticated
if (usernamePlaceholder) {
  const user = await checkAuth();
  if (!user) return;
  usernamePlaceholder.textContent = user.username;
}
nav(); //Initialize navigation bar
logout(); //Initialize logout button
});