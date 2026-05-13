import sqlite3
import os

from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'expense_tracker.db')


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id            INTEGER   PRIMARY KEY AUTOINCREMENT,
            name          TEXT      NOT NULL,
            email         TEXT      NOT NULL UNIQUE,
            password_hash TEXT      NOT NULL,
            created_at    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS expenses (
            id          INTEGER   PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER   NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            amount      REAL      NOT NULL CHECK (amount > 0),
            category    TEXT      NOT NULL,
            description TEXT,
            date        DATE      NOT NULL,
            created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()


def seed_db():
    conn = get_db()
    existing = conn.execute(
        "SELECT id FROM users WHERE email = 'priya@example.com'"
    ).fetchone()
    if existing:
        conn.close()
        return

    conn.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Priya Sharma", "priya@example.com", generate_password_hash("password123")),
    )
    conn.executemany(
        "INSERT INTO expenses (user_id, amount, category, description, date) VALUES (1,?,?,?,?)",
        [
            (250,  "Food",          "Lunch at office",    "2026-05-01"),
            (1200, "Transport",     "Monthly metro pass", "2026-05-01"),
            (3500, "Shopping",      "New shoes",          "2026-05-03"),
            (800,  "Bills",         "Electricity bill",   "2026-05-05"),
            (500,  "Entertainment", "Movie tickets",      "2026-05-08"),
        ],
    )
    conn.commit()
    conn.close()
