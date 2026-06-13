contacts = []

while True:
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)

        print("Contact Added Successfully!")

    elif choice == "2":
        print("\nContacts List")

        for contact in contacts:
            print(
                "Name:", contact["name"],
                "| Phone:", contact["phone"]
            )

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")