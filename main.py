from methods import EventManager
from user_auth import UserAuth

def main():
    print("Welcome to the Cultural Management System!")

    auth = UserAuth()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            auth.register(username, password)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if auth.login(username, password):
                print(f"Welcome back, {username}!")
                while True:
                    print("\n1. Proceed to Cultural Management")
                    print("2. Logout")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == "1":
                        cultural_management()
                        break
                    elif sub_choice == "2":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Try again.")
            else:
                print("Invalid login. Try again.")
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid input. Try again.")

def cultural_management():
    event_date = input("Enter the date for the cultural events (YYYY-MM-DD): ")
    manager = EventManager(event_date)

    while True:
        print("\n--- Event Management ---")
        print("1. View Events")
        print("2. Update Event Status")
        print("3. Delete Upcoming Event")
        print("4. Add New Event")
        print("5. Logout to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n1. View Upcoming Events")
            print("2. View Completed Events")
            view_choice = input("Enter your choice: ")
            if view_choice == "1":
                manager.view_events("upcoming")
            elif view_choice == "2":
                manager.view_events("completed")
            else:
                print("Invalid choice. Try again.")
        elif choice == "2":
            event_id = input("Enter the Event ID to update: ")
            status = input("Enter the status (completed/not completed): ").strip().lower()
            manager.update_status(event_id, status)
        elif choice == "3":
            event_id = input("Enter the Event ID to delete: ")
            manager.delete_event(event_id)
        elif choice == "4":
            event_name = input("Enter the Event Name: ")
            event_time = input("Enter the Event Time (HH:MM): ")
            manager.add_event(event_name, event_time)
        elif choice == "5":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
