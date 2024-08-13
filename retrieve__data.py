import sqlite3
from tabulate import tabulate

def retrieve_all_data():
    conn = sqlite3.connect('database_entry-exit.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM attendees')
    rows = cursor.fetchall()

    # Define table headers
    headers = ["ID", "Name", "Enrollment No.", "Entry Time", "Exit Time"]

    # Print the data in a tabular format
    print(tabulate(rows, headers, tablefmt="pretty"))

    conn.close()

if __name__ == "__main__":
    retrieve_all_data()
