import re
import json


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
    contact_edit = input("Enter the email of the contact you would like to edit: ")
    if contact_edit in contacts:
        while True:
            print("Current details:", contacts[contact_edit])
            category_to_edit = input("Enter a category to edit (name, phone, email, address, notes) or 'exit' to stop: ").lower()
            if category_to_edit == 'exit':
                break
            elif category_to_edit in contacts[contact_edit]:
                new_value = input(f"Enter the updated {category_to_edit}: ")
                contacts[contact_edit][category_to_edit] = new_value
                print(f"{category_to_edit.capitalize()} updated successfully.")
            else:
                print("Incorrect category, please try again.")
    else:
        print("Contact not found. Please check the email and try again.")

def delete_contact(contacts):
    contact_del = input("Enter the email of the contact you would like to delete: ")
    if contact_del in contacts:
        del contacts[contact_del]
        print(f"{contact_del} deleted successfully")
    else:
        print("Contact not found")

def search_contact(contacts):
    search_name = input("Enter the name of the contact you would like to search for: ")
    found = False

    for email, details in contacts.items():
        if details['name'] == search_name:
            found = True
            print(f"\n{search_name} details found:")
            print(f"Name: {details['name']}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {email}")  
            print(f"Address: {details['address']}")
            print(f"Notes: {details['notes']}")
            break 
    
    if not found:
        print(f"{search_name} does not exist in your contacts.\nPlease make sure you entered the name correctly and try again.")

def display_contacts(contacts):
    for email, details in contacts.items():
        name = details['name']
        phone = details['phone']
        address = details['address']
        notes = details['notes']
        
        print(f"\nEmail: {email}\nName: {name}\nPhone: {phone}\nAddress: {address}\nNotes: {notes}")

def export_contacts(contacts):
    filename = input("Enter the filename to export contacts to (default 'contacts.json'): ")
    if not filename:
        filename = 'contacts.json'
    try:
        with open(filename, 'w') as file:
            json.dump(contacts, file, indent=4)
        print(f"Contacts exported successfully to {filename}.")
    except IOError as e:
        print(f"Failed to write to file: {e}")

def get_contacts():
    with open('contacts.json', 'r') as file:
        contacts = json.load(file)
        print(contacts)
    return contacts

def main():
    contacts = get_contacts()
    while True:
        print("\nWelcome to the Contact Management System! Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Save changes to a JSON file")
        print("7. Exit")

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
            break
        else:
            print("Sorry that is an incompatable selection. Please try again.")\
            
main()