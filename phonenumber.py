import sqlite3


connection = sqlite3.connect("phonebook.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS entries (Name TEXT, Phone_number INTEGER)")

while True:
    print("\nWhat would you like to do?")
    print("1. Add user")
    print("2. List users")
    print("3. Update user")
    print("4. Delete user")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        name = str(input("please enter the name for the phone number: "))
        number = int(input("please enter the persons phone number: "))
        cursor.execute("INSERT INTO entries (Name, Phone_number) VALUES (?, ?)", (name, number))
        connection.commit()

    elif choice == "2":
        for row in cursor.execute("select * from entries"):
            print(row)

    elif choice == "3":
        update_name = str(input("please enter the first and last name of the entry you would like to edit: "))
        updated_name = str(input("please enter what you would like to change the name of the entry to: "))
        updated_number = int(input("please enter what you would like the change the name of the entry to: "))
        cursor.execute("UPDATE entries SET Name = ?, Phone_number = ? WHERE Name = ?",
                       (updated_name, updated_number, update_name))
        connection.commit()

    elif choice == "4":
        delete_entry = str(input("Please enter the name of the entry you would like to delete: "))
        cursor.execute("DELETE FROM entries WHERE Name = ?", (delete_entry,))
        connection.commit()
    elif choice == "5":

        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
