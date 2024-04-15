def add_new_contact():
    pass

def edit_contact():
    pass

def delete_contact():
    pass

def search_contact():
    pass

def display_contacts():
    pass

def export_contacts():
    pass

def import_contacts():
    pass

def read_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts = {}
            for line in file:
                try: name, number, email, adress = line.strip().split(',')

                except ValueError:
                    print(f"Error Processing line: {line.strip()}")
            return contacts
    except FileNotFoundError:
        print("File not found")
        return{}


def contact_manager():
    contacts = read_contacts('contacts.txt')


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



def main():
    while True:
        print("Welcome to the Contact Management System! Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")

        choice = input("Enter your selection here")
        if choice == '1':
            add_new_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice =='5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            break
        else:
            print("Sorry that is an incompatable selection. Please try again.")

main()