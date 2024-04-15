import re


def add_new_contact(contacts):
    email = input("Enter contact's email: ").strip()

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format.")
        return
    
    if email in contacts:
        print("Contact with this email already exists.")
        return
    
    name = input("Enter the contact's name: ")
    phone = input("Enter contact's phone number: ").strip()
    if not re.match(r"\+?[1-9]\d{1,14}$", phone):
        print("Invalid phone number format.")
        return
    adress = input("Enter contact's address: ").strip()
    notes = input("Enter additional notes (optional): ").strip()

    contacts[email] = {
        'name': name, 
        'phone': phone,
        'address': adress,
        'notes': notes
    }

    print(f"Contact {name} added successfully")

def edit_contact(contacts):
    pass

def delete_contact(contacts):
    contact_del = input("Enter the email of the contact you would like to delete: ")
    if contact_del in contacts:
        del contacts[contact_del]
        print(f"{contact_del} deleted successfully")
    else:
        print("Contact not found")

def search_contact():
    pass

def display_contacts(contacts):
    for email, details in contacts.items():
        name = details['name']
        phone = details['phone']
        address = details['address']
        notes = details['notes']
        
        print(f"\nEmail: {email}\nName: {name}\nPhone: {phone}\nAddress: {address}\nNotes: {notes}")

def export_contacts():
    pass

def import_contacts():
    pass

def main():
    contacts = {
    "alice.brown@example.com": {
        "name": "Alice Brown",
        "phone": "+11234567890",
        "address": "123 Cherry Lane, Springfield, USA",
        "notes": "Met at a conference."
    },
    "bob.smith@example.com": {
        "name": "Bob Smith",
        "phone": "+10987654321",
        "address": "456 Maple Street, South Park, USA",
        "notes": "Colleague from work."
    },
    "carol.jones@example.com": {
        "name": "Carol Jones",
        "phone": "+1230984567",
        "address": "789 Pine Road, Gotham, USA",
        "notes": "Family friend."
    },
     "david.green@example.com": {
        "name": "David Green",
        "phone": "+18001234567",
        "address": "101 Oak Street, Metropolis, USA",
        "notes": "Gym buddy."
    },
    "eva.white@example.com": {
        "name": "Eva White",
        "phone": "+18007654321",
        "address": "202 Birch Avenue, Smallville, USA",
        "notes": "Met during a workshop."
    },
    "frank.moore@example.com": {
        "name": "Frank Moore",
        "phone": "+18009876543",
        "address": "303 Cedar Blvd, Star City, USA",
        "notes": "Neighbor."
    }
}
    while True:
        print("\nWelcome to the Contact Management System! Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")

        choice = input("Enter your selection here: ")
        if choice == '1':
            add_new_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice =='5':
            display_contacts(contacts)
        elif choice == '6':
            export_contacts(contacts)
        elif choice == '7':
            import_contacts(contacts)
        elif choice == '8':
            break
        else:
            print("Sorry that is an incompatable selection. Please try again.")

main()