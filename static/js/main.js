(function () {
    const toggle = document.getElementById('themeToggle');
    const dropdown = document.getElementById('themeDropdown');
    const picker = document.getElementById('themePicker');
    const opts = document.querySelectorAll('.theme-opt');
    if (!toggle || !dropdown) return;

    function getTheme() {
        return document.documentElement.getAttribute('data-theme') || 'light';
    }

    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        opts.forEach(function (opt) {
            opt.classList.toggle('active', opt.dataset.theme === theme);
        });
    }

    applyTheme(getTheme());

    toggle.addEventListener('click', function (e) {
        e.stopPropagation();
        dropdown.classList.toggle('open');
    });

    opts.forEach(function (opt) {
        opt.addEventListener('click', function () {
            applyTheme(this.dataset.theme);
            dropdown.classList.remove('open');
        });
    });

    document.addEventListener('click', function (e) {
        if (!picker.contains(e.target)) {
            dropdown.classList.remove('open');
        }
    });
})();
