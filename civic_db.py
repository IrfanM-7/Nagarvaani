import sqlite3
from datetime import datetime
import random

DB_NAME = "complaints.db"

# -------------------------------
# Initialize the database
# -------------------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            complaint_id TEXT PRIMARY KEY,
            title TEXT,
            description TEXT,
            category TEXT,
            date TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()


# -------------------------------
# Add a new complaint
# -------------------------------
def add_complaint(description):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Auto-detect category (Tamil keywords)
    if "தண்ணீர்" in description:
        category = "தண்ணீர்"
    elif "சாலை" in description:
        category = "சாலை"
    elif "மின்சாரம்" in description:
        category = "மின்சாரம்"
    elif "குப்பை" in description:
        category = "குப்பை"
    else:
        category = "மற்றவை"

    complaint_id = f"CMP{random.randint(1000000000,9999999999)}"
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    status = "புதியது"

    cur.execute("INSERT INTO complaints VALUES (?, ?, ?, ?, ?, ?)",
                (complaint_id, description[:20], description, category, date, status))
    conn.commit()
    conn.close()

    return complaint_id, category, date, status


# -------------------------------
# List all complaints
# -------------------------------
def list_complaints():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaints")
    data = cur.fetchall()
    conn.close()
    return data
