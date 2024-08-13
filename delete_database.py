import os

def delete_database():
    db_file = 'database_entry-exit.db'

    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Database '{db_file}' has been deleted.")
    else:
        print(f"Database '{db_file}' does not exist.")

if __name__ == "__main__":
    delete_database()
