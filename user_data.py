import sqlite3
import os

# User data processor
DB_PASSWORD = os.environ.get('DB_PASSWORD')
API_KEY = os.environ.get('API_KEY')

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