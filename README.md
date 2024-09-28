# Banking Simulation System

A Python-based banking system that allows users to securely sign up, log in, and perform essential banking transactions such as deposits, withdrawals, and balance checks. This system focuses on data security using hashed passwords and provides an intuitive interface for basic financial operations.

## Features

- **User Authentication**: Secure sign-up and login using **bcrypt** for password hashing.
- **Transactions**: Supports deposits, withdrawals, and balance checking for users.
- **Data Persistence**: User data and transaction records are stored using **SQLite**.
- **Modular Design**: The project is organized into different modules for authentication, transactions, and database management.

## Technologies

- **Python**: Core programming language.
- **SQLite**: Database for user data management.
- **bcrypt**: For secure password hashing.

## Setup and Installation

### Prerequisites
- Python 3.x installed on your system.
- Install the required Python libraries by running:
  ```bash
  pip install bcrypt sqlite3
  ```

### Step-by-Step Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Enocko/banking-simulation-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd banking-simulation-system
   ```

3. Run the main program:
   ```bash
   python main.py
   ```

### Database Setup
The SQLite database is automatically created when you run the project for the first time. The `db.py` file sets up the necessary tables.

## Usage

1. **Sign Up**: Users can create an account by choosing a unique username and password. Passwords are securely hashed before storage.
2. **Login**: Users can log in with their username and password to access their account.
3. **Banking Operations**:
   - **Deposit**: Add funds to your account.
   - **Withdraw**: Withdraw funds from your account, ensuring sufficient balance.
   - **Check Balance**: View your current account balance.

## Future Improvements

- Add transaction history for users to review past operations.
- Implement password recovery for better user experience.
- Expand the system to include more advanced banking operations like transfers between users.

