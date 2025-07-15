import re

from typing import List


class Contact:
    """
    Represents a simple entry for the Contact Manager
    """

    def __init__(self, name: str, email_address: str, phone: str):
        """
        Initializes a contact.

        Args:
            name (str): Contact's name.
            email (str): Contact's email.
            phone (str): Contact's phone
        """
        self.name = name
        self._email = ""
        self.email = email_address
        self.phone = phone

    @property
    def email(self):
        """
        Get contact's name
        """
        return self._email

    # Validating email
    @email.setter
    def email(self, email_address: str):
        """
        Set the contact's email. Validating the address
        """
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        if not re.match(pattern, email_address):
            raise ValueError("Email not valid")
        self._email = email_address


class ContactManager:
    """
    Represents the list with all the contacts, with methods to add, remove, search by name and export contacts to CSV
    """

    def __init__(self):
        self._contacts: List[Contact] = []

    def __len__(self) -> int:
        """
        Return number of contacts.
        """
        return len(self._contacts)

    def __iter__(self):
        """
        Allow iteration over contacts.
        """
        return iter(self._contacts)

    def add_contact(self, contact: Contact):
        self._contacts.append(contact)

    def remove_contact(self, name: str) -> bool:
        """
        Remove first contact matching name. Return True if removed.
        """
        for i, c in enumerate(self._contacts):
            if c.name == name:
                del self._contacts[i]
                return True
        return False

    def search(self, name: str) -> List[Contact]:
        """
        Return contacts with matching or partial name.
        """
        name_lower = name.lower()
        return [c for c in self._contacts if name_lower in c.name.lower()]


if __name__ == "__main__":
    book = ContactManager()

    contact1 = Contact("Felipe", "afmejia23@gmail.com", "3217845263")
    book.add_contact(contact1)

    print(len(book))
    for contact in book:
        print(contact.name, " ", contact.email)
