CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id BIGINT UNIQUE,
    username TEXT,
    uid TEXT,
    league TEXT DEFAULT 'EDGE base',
    points INTEGER DEFAULT 0
);
