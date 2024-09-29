import bcrypt
from db import cursor, conn

# Sign-up function to create a new user account
def sign_up():
    username = input("Enter a new username: ")
    password = input("Create a password: ")

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        # Insert the user into the database
        cursor.execute("INSERT INTO users (username, password, balance) VALUES (?, ?, ?)", 
                       (username, hashed_password, 0))  # Default balance = 0
        conn.commit()
        print("Account created successfully!")
    except Exception as e:
        print(f"Error: {e}. Username may already exist. Please try again.")

# Login function to authenticate an existing user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user:
        stored_password = user[0]
        # Check if the entered password matches the stored hashed password
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            print("Login successful!")
            return username
        else:
            print("Incorrect password.")
            return None
    else:
        print("Username not found.")
        return None

# Password setup (can be replaced with the login function)
def setup_password():
    for attempt in range(3, 0, -1):
        password = input("Please enter your card PIN: ")
        if password == "1234":  # Hardcoded PIN for now, can be linked with login in the future
            break
        else:
            print("Wrong password")
    if attempt == 1 and password != "1234":
        print("Access denied")
        quit()
    else:
        print('Access Granted')
