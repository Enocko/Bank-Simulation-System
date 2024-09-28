from db import cursor, conn

def deposit(username, amount):
    cursor.execute("UPDATE users SET balance = balance + ? WHERE username = ?", (amount, username))
    conn.commit()
    print(f"An amount of ${amount} has been deposited.")

def withdraw(username, amount):
    cursor.execute("SELECT balance FROM users WHERE username = ?", (username,))
    balance = cursor.fetchone()[0]

    if amount > balance:
        print("Insufficient funds!")
    else:
        cursor.execute("UPDATE users SET balance = balance - ? WHERE username = ?", (amount, username))
        conn.commit()
        print(f"An amound of ${amount} has been withdrawn.")

def check_balance(username):
    cursor.execute("SELECT balance FROM users WHERE username = ?", (username,))
    balance = cursor.fetchone()[0]
    print(f"Your current balance is ${balance}")

def user_actions(username):
    while True:
        print('      Please how may we help you.............????????      ')
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout")
        print('      Which transaction will you like to make.....????????      ')
        choice = input("Please make a choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            deposit(username, amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            withdraw(username, amount)
        elif choice == '3':
            check_balance(username)
        elif choice == '4':
            print("      <<<<<<<<<<<<<Thank you for choosing our service<<<<<<<<<<<<<<   ")
            break
        else:
            print("Invalid choice. Try again.")
        print()
