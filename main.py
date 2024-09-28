from auth import sign_up, login
from transactions import user_actions
from db import setup_db

def main():
    print("               <<<<<<<<<<<<<< Welcome to World bank <<<<<<<<<<<<<<              ")
    while True:
        print("\n1. Login\n2. Sign Up\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = login()  # Login and return the username if successful
            if username:
                user_actions(username)  # Pass the username for transactions
        elif choice == '2':
            sign_up()  # Sign up for a new account
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    setup_db()  # Ensure the database is set up before starting
    main()
