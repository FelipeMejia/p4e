import sqlite3

from pathlib import Path
from sqlite3 import Connection, Cursor


class ContactsManager:
    def __init__(self, db_path: str = "contacts.sqlite"):
        self.db_path = db_path
        self._conn: Connection = sqlite3.connect(db_path)
        self._cur: Cursor = self._conn.cursor()

    def create_contacts_table(self) -> bool:
        try:
            self._cur.execute(
                """
                CREATE TABLE IF NOT EXISTS Contacts (
                    id INTEGER PRIMARY KEY, 
                    name TEXT NOT NULL, 
                    email TEXT UNIQUE NOT NULL, 
                    phone TEXT)
                """
            )
            self._conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error creating Contacts table:", e)
            return False

    def add_contact(self, name: str, email: str, phone: str) ->:
        try:
            self._cur.execute(
                """
                INSERT INTO Contacts (name, email, phone)
                VALUES (?, ?, ?)
                """,
                (name, email, phone),
            )
            self._conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"⚠️ Duplicate email skipped: {email}")
            return False
        except sqlite3.Error as e:
            print(f"❌ Failed to insert contact {email}: {e}")
            return False
    
    def get_all_contacts(self) -> list[tuple]:
        return self._cur.execute("SELECT * FROM Contacts").fetchall()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type:
            self._conn.rollback()
        else:
            self._conn.commit()
        self._conn.close()


if __name__ == "__main__":
    # Make sure database file exists; let sqlite3.create if not
    db_file = Path("contacts.sqlite")
    if db_file.exists():
        print(f"✅ Database file {db_file} found.")
    else:
        print(f"➡️ Creating new database at {db_file}")

    sample_contacts = [
        ("Bruce Lee", "bruce@example.com", "555-0100"),
        ("Jim Carrie", "themask@example.com", "555-0200"),
        ("Adam Sandler", "clown@example.com", "555-0300"),
    ]

    with ContactsManager() as manager:
        if manager.create_contacts_table():
            print("✅ Contacts table ready.")
        else:
            print("❌ Failed to create Contacts table.")
            exit(1)

        for name, email, phone in sample_contacts:
            manager.add_contact(name, email, phone)

        rows = manager.get_all_contacts()
        print("\n📇 Current contacts in database:")
        for row in rows:
            print(row)

        # with sqlite3.connect("contacts.sqlite") as conn:
        #     cur = conn.cursor()
        #     for name, email, phone in sample_contacts:
        #         try:
        #             cur.execute(
        #                 """
        #                 INSERT INTO Contacts (name, email, phone)
        #                 VALUES (?, ?, ?)
        #                 """,
        #                 (name, email, phone),
        #             )
        #         except sqlite3.IntegrityError as e:
        #             print(f"⚠️  Skipped inserting {email}: {e}")

        # # Verify insertion
        # with sqlite3.connect("contacts.sqlite") as conn:
        # cur = conn.cursor()
        # rows = cur.execute("SELECT * FROM Contacts").fetchall()
        # print("\n📇 Current contacts in database:")
        # for row in rows:
        #     print(row)
