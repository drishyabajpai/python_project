import json #it is a built-in module in Python that provides functions for working with JSON data. It allows you to convert Python objects to JSON format and vice versa.
import os # os is a built-in module in Python that provides a way to interact with the operating system. It allows you to perform various tasks such as file and directory manipulation, environment variable access, and process management.

FILE_NAME = "contacts.json"


# ---------------------------
# Load Contacts
# ---------------------------
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


# ---------------------------
# Save Contacts
# ---------------------------
def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()


# ---------------------------
# Add Contact
# ---------------------------
def add_contact():
    name = input("Enter Name: ").strip()

    if name in contacts:
        print("❌ Contact already exists!")
        return

    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email
    }

    save_contacts()

    print("✅ Contact Added Successfully!")


# ---------------------------
# View Contacts
# ---------------------------
def view_contacts():
    if not contacts:
        print("\nNo Contacts Found.\n")
        return

    print("\n========== CONTACT LIST ==========")

    for name in sorted(contacts):
        print(f"\nName  : {name}")
        print(f"Phone : {contacts[name]['Phone']}")
        print(f"Email : {contacts[name]['Email']}")


# ---------------------------
# Search Contact
# ---------------------------
def search_contact():
    name = input("Enter Name: ")

    if name in contacts:
        print("\nContact Found")
        print("----------------------")
        print("Name :", name)
        print("Phone:", contacts[name]["Phone"])
        print("Email:", contacts[name]["Email"])
    else:
        print("❌ Contact Not Found.")


# ---------------------------
# Update Contact
# ---------------------------
def update_contact():
    name = input("Enter Name to Update: ")

    if name not in contacts:
        print("❌ Contact Not Found.")
        return

    phone = input("New Phone: ")
    email = input("New Email: ")

    contacts[name]["Phone"] = phone
    contacts[name]["Email"] = email

    save_contacts()

    print("✅ Contact Updated Successfully.")


# ---------------------------
# Delete Contact
# ---------------------------
def delete_contact():
    name = input("Enter Name to Delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts()
        print("🗑 Contact Deleted Successfully.")
    else:
        print("❌ Contact Not Found.")


# ---------------------------
# Main Menu
# ---------------------------
while True:

    print("\n==============================")
    print("      CONTACT BOOK")
    print("==============================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nThank You For Using Contact Book ❤️")
        break

    else:
        print("❌ Invalid Choice.")