(function () {
    const toggle = document.getElementById('themeToggle');
    if (!toggle) return;

    function getTheme() {
        return document.documentElement.getAttribute('data-theme') || 'light';
    }

    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        toggle.textContent = theme === 'dark' ? '☀' : '☽';
        toggle.title = theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';
        localStorage.setItem('theme', theme);
    }

    applyTheme(getTheme());

    toggle.addEventListener('click', function () {
        applyTheme(getTheme() === 'dark' ? 'light' : 'dark');
    });
})();
