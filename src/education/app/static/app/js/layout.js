const refresh = () => {
    window.location.reload()
    console.log("refreshed");
}
const logout = () => {
    const logoutForm = document.getElementById("logoutForm")
    logoutForm.submit()
}
const themeToggle = document.getElementById('themeToggle');
const lightTheme = document.getElementById("light-theme");
const darkTheme = document.getElementById("dark-theme");

const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)').matches;

let theme = localStorage.getItem("theme");

if (theme === "auto") {
    theme = prefersDarkScheme ? "dark" : "light";
}

if (theme === null) {
    theme = "light"; // Default
    localStorage.setItem("theme", theme);
}

applyTheme(theme);

function toggleTheme() {
    const newTheme = localStorage.getItem("theme") === "light" ? "dark" : "light";
    setTheme(newTheme);
}

function setTheme(newTheme) {
    localStorage.setItem("theme", newTheme);
    applyTheme(newTheme);
}

function applyTheme(theme) {
    const isDark = theme === "dark";
    darkTheme.disabled = !isDark;
    lightTheme.disabled = isDark;

    // Update button text and icon
    themeToggle.innerHTML = `
        ${isDark ? 'Light' : 'Dark'} Mode
        <nord-icon slot="end" name="interface-mode-${isDark ? 'light' : 'dark'}"></nord-icon>
    `;
}


 document.addEventListener('DOMContentLoaded', () => {
      const loadingScreen = document.getElementById('loading-screen');
      const mainLayout = document.getElementById('main-layout');

      window.addEventListener('load', () => {
        // Fade out loading screen
        loadingScreen.classList.add('opacity-0');
        
        // Fade in main layout
        mainLayout.classList.remove('opacity-0');
        
        // Remove loading screen after transition
        setTimeout(() => {
          loadingScreen.remove();
        }, 300);
      });
    });