const lightBtn = document.getElementById('lightBtn');
const darkBtn = document.getElementById('darkBtn');

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

lightBtn.addEventListener("click", () => {
    setTheme("light");
});

darkBtn.addEventListener("click", () => {
    setTheme("dark");
});

function setTheme(newTheme) {
    localStorage.setItem("theme", newTheme);
    applyTheme(newTheme);
}

function applyTheme(theme) {
    if (theme === "dark") {
        darkTheme.disabled = false;
        lightTheme.disabled = true;

        // Show the light button to switch back
        lightBtn.style.display = "inline-block";
        darkBtn.style.display = "none";
    } else {
        darkTheme.disabled = true;
        lightTheme.disabled = false;

        // Show the dark button to switch back
        lightBtn.style.display = "none";
        darkBtn.style.display = "inline-block";
    }
}
