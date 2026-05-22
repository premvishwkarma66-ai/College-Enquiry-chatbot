CREATE TABLE IF NOT EXISTS faq (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    category TEXT,
    created_on DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE,
  password TEXT,
  role TEXT   -- "admin" or "user"
);
INSERT INTO users (email, password, role)
VALUES ('admin@college.com', 'admin123', 'admin');

INSERT INTO users (email, password, role)
VALUES ('user@gmail.com', 'user123', 'user');

