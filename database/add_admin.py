from core.db import get_db

conn = get_db()
cur = conn.cursor()

cur.execute("""
INSERT INTO admin_users (name, email, password)
VALUES ('Admin', 'admin@chatbot.com', 'admin123')
""")

conn.commit()
conn.close()

print("Default admin created")
