import sqlite3

def add_entry():
    name = input("Enter name: ")
    enrollment_no = input("Enter enrollment number: ")

    conn = sqlite3.connect('freshers_party.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO attendees (name, enrollment_no) 
    VALUES (?, ?)
    ''', (name, enrollment_no))

    conn.commit()
    conn.close()
    print(f"Entry added for {name}.")

def edit_entry():
    enrollment_no = input("Enter enrollment number to edit: ")
    new_name = input("Enter new name: ")

    conn = sqlite3.connect('freshers_party.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE attendees 
    SET name = ? 
    WHERE enrollment_no = ?
    ''', (new_name, enrollment_no))

    conn.commit()
    conn.close()
    print(f"Entry updated for enrollment number {enrollment_no}.")

def delete_entry():
    enrollment_no = input("Enter enrollment number to delete: ")

    conn = sqlite3.connect('freshers_party.db')
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM attendees 
    WHERE enrollment_no = ?
    ''', (enrollment_no,))

    conn.commit()
    conn.close()
    print(f"Entry deleted for enrollment number {enrollment_no}.")

def view_entries():
    conn = sqlite3.connect('freshers_party.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM attendees')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def main():
    while True:
        print("1. Add Entry")
        print("2. Edit Entry")
        print("3. Delete Entry")
        print("4. View Entries")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            edit_entry()
        elif choice == '3':
            delete_entry()
        elif choice == '4':
            view_entries()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
