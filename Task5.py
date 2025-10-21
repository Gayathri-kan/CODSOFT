# CONTACT BOOK - TASK 5
# Created by Darlo 💻

contacts = {}

def add_contact():
    name = input("Enter Name: ").strip().title()
    if name in contacts:
        print("Contact already exists!")
        return
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"\n✅ Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("\n📭 No contacts found.\n")
        return
    print("\n📒 Contact List:")
    print("-" * 40)
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
        print(f"Address: {info['Address']}")
        print("-" * 40)

def search_contact():
    search = input("Enter name or phone to search: ").strip().lower()
    found = False
    for name, info in contacts.items():
        if search in name.lower() or search in info["Phone"]:
            print("\n🔍 Contact Found:")
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}")
            found = True
    if not found:
        print("\n❌ No matching contact found!\n")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip().title()
    if name not in contacts:
        print("\n❌ Contact not found!\n")
        return
    print("\nLeave blank to keep existing value.\n")
    phone = input(f"New Phone ({contacts[name]['Phone']}): ").strip()
    email = input(f"New Email ({contacts[name]['Email']}): ").strip()
    address = input(f"New Address ({contacts[name]['Address']}): ").strip()
    if phone:
        contacts[name]["Phone"] = phone
    if email:
        contacts[name]["Email"] = email
    if address:
        contacts[name]["Address"] = address
    print(f"\n✅ Contact '{name}' updated successfully!\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        print(f"\n🗑️ Contact '{name}' deleted successfully!\n")
    else:
        print("\n❌ Contact not found!\n")

def menu():
    while True:
        print("==== CONTACT BOOK ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("======================")
        choice = input("Enter your choice (1-6): ").strip()

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
            print("\n👋 Exiting Contact Book. Goodbye!\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please enter a number between 1 and 6.\n")

# Run the program
menu()
