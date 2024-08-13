import sqlite3

conn = sqlite3.connect('database_entry-exit.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS attendees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    enrollment_no TEXT NOT NULL,
    entry_time TEXT,
    exit_time TEXT
)
''')

conn.commit()
conn.close()
