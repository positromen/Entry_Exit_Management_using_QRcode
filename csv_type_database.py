import csv
import sqlite3

def create_table():
    conn = sqlite3.connect('freshers_party.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        enrollment_no TEXT UNIQUE NOT NULL,
        entry_time TEXT,
        exit_time TEXT
    )
    ''')

    conn.commit()
    conn.close()

def insert_entries_from_csv(csv_file):
    conn = sqlite3.connect('freshers_party.db')
    cursor = conn.cursor()

    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        # Prepare the data for insertion
        entries = [(row['name'], row['enrollment_no']) for row in reader]
        
        # Insert data into the database
        cursor.executemany('''
        INSERT OR IGNORE INTO attendees (name, enrollment_no) VALUES (?, ?)
        ''', entries)

    conn.commit()
    conn.close()
    print(f"Data from {csv_file} has been inserted.")

if __name__ == "__main__":
    create_table()  # Create table if it doesn't exist
    insert_entries_from_csv('entries.csv')
