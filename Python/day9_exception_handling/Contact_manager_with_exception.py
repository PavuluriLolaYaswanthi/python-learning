#Contact Manager, Hardened
#Take your Contact Manager from before and add error handling so that:
#Loading contacts from a file that doesn't exist yet doesn't crash — it just starts with an empty list
import os
contacts = []
def load_contacts():
    try:
        if not os.path.exists("contacts.txt"):
            with open("contacts.txt","r") as file:
                for line in file:
                    name,phone = line.strip().split(",")
                    contacts.append({"name": name, "phone": phone})
        else:
            print("Contacts file not found. Starting with an empty contact list.")
    except Exception as e:
        print("An error occurred while loading contacts:", e)
def remove_contact(name):
    try:
        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print(f"Contact {name} removed.")
                return
        raise ValueError(f"Contact {name} not found.")
    except ValueError as e:
        print(e)
def save_contacts():
    try:
        with open("contacts.txt", "w") as file:
            for contact in contacts:
                file.write(f"{contact['name']},{contact['phone']}\n")
    except Exception as e:
        print("An error occurred while saving contacts:", e)
load_contacts()
remove_contact("John Doe")  # Example of removing a contact
save_contacts()  # Example of saving contacts