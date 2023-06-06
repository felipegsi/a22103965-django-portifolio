function toggleDarkMode() {
  const button = document.getElementById('dark-mode-button');
  const body = document.body;

  button.addEventListener('click', function () {
    body.classList.toggle('dark-mode');
  });
}
