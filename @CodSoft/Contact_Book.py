class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}

    def view_contact_list(self):
        print("\nContact List:")
        for name, details in self.contacts.items():
            print(f"{name}: {details['phone_number']}")

    def search_contact(self, keyword):
        matching_contacts = {name: details for name, details in self.contacts.items() if keyword in name or keyword in details['phone_number']}
        if matching_contacts:
            print("\nMatching Contacts:")
            for name, details in matching_contacts.items():
                print(f"{name}: {details['phone_number']}")
        else:
            print("\nNo matching contacts found.")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        if name in self.contacts:
            self.contacts[name] = {'phone_number': new_phone_number, 'email': new_email, 'address': new_address}
            print(f"\nContact '{name}' updated successfully.")
        else:
            print(f"\nContact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"\nContact '{name}' deleted successfully.")
        else:
            print(f"\nContact '{name}' not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_manager.view_contact_list()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_manager.search_contact(keyword)

        elif choice == '4':
            name = input("Enter contact name to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_manager.update_contact(name, new_phone_number, new_email, new_address)

        elif choice == '5':
            name = input("Enter contact name to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
