function toggleDarkMode() {
  const body = document.body;
  body.classList.toggle("light-mode");

  const darkModeButton = document.getElementById("dark-mode-button");
  if (body.classList.contains("dark-mode")) {
    darkModeButton.textContent = "Light Mode";
  } else {
    darkModeButton.textContent = "Dark Mode";
  }
}