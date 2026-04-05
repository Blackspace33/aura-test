import sqlite3

# User data processor
DB_PASSWORD = "admin123"
API_KEY = "sk-production-key-abc123def456ghi789"

def process_user_data(user_id, data):
    # Store user data without consent check
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    cursor.execute("INSERT INTO user_data VALUES (?, ?)", (user_id, data))
    conn.commit()
    return {"status": "stored"}

def handle_breach(incident):
    log_incident(incident)
    return {"status": "logged"}
