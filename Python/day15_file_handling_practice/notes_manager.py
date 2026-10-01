while True:
    print("\n====== Notes Manager ======")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        note = input("Enter your note: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        print("Note added successfully.")
    
    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                notes = file.read()
                if notes:
                    print("\nYour Notes:")
                    print(notes)
                else:
                    print("No notes found.")
        except FileNotFoundError:
            print("No notes found.")
    
    elif choice == "3":
        print(" Exit ")
        break
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")