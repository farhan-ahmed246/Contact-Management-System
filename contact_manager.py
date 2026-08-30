import json
from pathlib import Path

DATA_FILE = Path("contacts.json")


def load_contacts():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_contacts(contacts):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for index, contact in enumerate(contacts, start=1):
        print(f"\n{index}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")


def search_contacts(contacts):
    query = input("Search name or phone: ").strip().lower()
    matches = [c for c in contacts if query in c['name'].lower() or query in c['phone'].lower()]
    if not matches:
        print("No matching contacts found.")
        return
    for contact in matches:
        print(f"{contact['name']} | {contact['phone']} | {contact['email']}")


def delete_contact(contacts):
    try:
        index = int(input("Contact number to delete: ")) - 1
        contacts.pop(index)
    except (ValueError, IndexError):
        print("Invalid contact number.")
        return
    save_contacts(contacts)
    print("Contact deleted successfully.")


def main():
    contacts = load_contacts()
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contacts")
        print("4. Delete contact")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1": add_contact(contacts)
        elif choice == "2": view_contacts(contacts)
        elif choice == "3": search_contacts(contacts)
        elif choice == "4": delete_contact(contacts)
        elif choice == "5": break
        else: print("Invalid option.")


if __name__ == "__main__":
    main()
