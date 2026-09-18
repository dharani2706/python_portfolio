const themeToggle = document.getElementById("themeToggle");
const root = document.documentElement;
const storedTheme = localStorage.getItem("portfolio-theme");

function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    localStorage.setItem("portfolio-theme", theme);
    if (themeToggle) {
        themeToggle.innerHTML =
            theme === "dark"
                ? '<i class="bi bi-sun"></i>'
                : '<i class="bi bi-moon-stars"></i>';
    }
}

const preferredTheme =
    storedTheme ||
    (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
applyTheme(preferredTheme);

if (themeToggle) {
    themeToggle.addEventListener("click", () => {
        const nextTheme = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
        applyTheme(nextTheme);
    });
}

document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (event) => {
        const target = document.querySelector(link.getAttribute("href"));
        if (!target) {
            return;
        }
        event.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
});
