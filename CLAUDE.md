# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the dev server (localhost:5001)
python app.py

# Run all tests
pytest

# Run a single test file
pytest tests/test_auth.py

# Install dependencies
pip install -r requirements.txt
```

## Architecture

**Spendly** is a Flask-based personal expense tracker targeted at Indian users (₹ currency). The project is in early MVP — the frontend/UI is complete, but authentication and expense logic are not yet implemented.

### Stack

- **Backend:** Flask 3.1.3, Python — entry point is `app.py`
- **Templates:** Jinja2, extending `templates/base.html`
- **Database:** SQLite (planned) via `database/db.py` — `get_db()`, `init_db()`, `seed_db()` are stubs
- **Frontend:** Vanilla JS + custom CSS; no Node.js toolchain
- **Tests:** pytest + pytest-flask

### Route status

Routes returning real pages: `/`, `/login`, `/register`, `/terms`, `/privacy`.  
Stubbed routes (return placeholder): `/logout`, `/profile`, `/expenses/add`, `/expenses/<id>/edit`, `/expenses/<id>/delete`.

### Theming system

`static/css/style.css` uses CSS custom properties to implement 5 themes (light, dark, ocean, sunset, violet). Theme selection is persisted in `localStorage` via `static/js/main.js`. To add a new theme, add a `[data-theme="name"]` block in the variables section of `style.css` and a corresponding entry in the theme picker in `base.html`.

### Template layout

All pages extend `templates/base.html`, which provides the navbar (with theme picker) and footer. `landing.html` has its own supplemental stylesheet at `static/css/landing.css`.

### Database

`database/db.py` stubs need to be filled in before any auth or expense routes can persist data. The SQLite file (`expense_tracker.db`) is git-ignored. When implementing, enable foreign keys with `PRAGMA foreign_keys = ON` on each connection.
