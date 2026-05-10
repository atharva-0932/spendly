# Database Specification — Step 1: Database Setup

## Overview

Spendly uses **SQLite** as its database. All database logic lives in `database/db.py`.  
The SQLite file (`expense_tracker.db`) is git-ignored and lives at the project root.

---

## Schema

### `users`

Stores registered accounts.

| Column          | Type         | Constraints                        |
|-----------------|--------------|------------------------------------|
| `id`            | INTEGER      | PRIMARY KEY AUTOINCREMENT          |
| `name`          | TEXT         | NOT NULL                           |
| `email`         | TEXT         | NOT NULL, UNIQUE                   |
| `password_hash` | TEXT         | NOT NULL                           |
| `created_at`    | TIMESTAMP    | NOT NULL, DEFAULT CURRENT_TIMESTAMP |

### `expenses`

Stores individual expense records, linked to a user.

| Column        | Type      | Constraints                                      |
|---------------|-----------|--------------------------------------------------|
| `id`          | INTEGER   | PRIMARY KEY AUTOINCREMENT                        |
| `user_id`     | INTEGER   | NOT NULL, FOREIGN KEY → `users(id)` ON DELETE CASCADE |
| `amount`      | REAL      | NOT NULL, CHECK (amount > 0)                     |
| `category`    | TEXT      | NOT NULL                                         |
| `description` | TEXT      |                                                  |
| `date`        | DATE      | NOT NULL                                         |
| `created_at`  | TIMESTAMP | NOT NULL, DEFAULT CURRENT_TIMESTAMP              |

**Valid categories:** `Food`, `Transport`, `Shopping`, `Bills`, `Health`, `Entertainment`, `Other`

---

## Functions to Implement

### `get_db()`

Returns a SQLite connection configured for use in Flask routes.

**Requirements:**
- Open `expense_tracker.db` at the project root
- Set `row_factory = sqlite3.Row` so columns are accessible by name
- Execute `PRAGMA foreign_keys = ON` on every connection
- Return the connection

```python
def get_db():
    # returns sqlite3.Connection
```

---

### `init_db()`

Creates all tables if they don't already exist. Safe to call on every app start.

**Requirements:**
- Use `CREATE TABLE IF NOT EXISTS` for both `users` and `expenses`
- Apply all constraints from the schema above
- Commit and close the connection when done

```python
def init_db():
    # returns None
```

---

### `seed_db()`

Inserts sample data for local development and testing. Should be idempotent (skip if data already exists).

**Requirements:**
- Insert at least 1 sample user (hashed password — use `werkzeug.security.generate_password_hash`)
- Insert at least 5 sample expenses across different categories and dates
- Use `INSERT OR IGNORE` or check row count before inserting to avoid duplicates

**Sample user:**

| Field    | Value                   |
|----------|-------------------------|
| name     | Priya Sharma            |
| email    | priya@example.com       |
| password | password123 (hashed)    |

**Sample expenses (user_id = 1):**

| Amount (₹) | Category      | Description          | Date       |
|------------|---------------|----------------------|------------|
| 250        | Food          | Lunch at office      | 2026-05-01 |
| 1200       | Transport     | Monthly metro pass   | 2026-05-01 |
| 3500       | Shopping      | New shoes            | 2026-05-03 |
| 800        | Bills         | Electricity bill     | 2026-05-05 |
| 500        | Entertainment | Movie tickets        | 2026-05-08 |

---

## Usage in `app.py`

Call `init_db()` once at startup, before the app starts serving requests:

```python
from database.db import init_db

with app.app_context():
    init_db()
```

Call `seed_db()` only in development — guard it behind an environment check or a CLI flag.

---

## File Location

```
expense-tracker/
├── database/
│   ├── __init__.py
│   └── db.py          ← implement get_db(), init_db(), seed_db() here
├── expense_tracker.db  ← created at runtime, git-ignored
└── docs/
    └── database_spec.md
```
