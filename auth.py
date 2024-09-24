import sqlite3
import hashlib
import os

def create_connection():
    conn = sqlite3.connect('finance_app.db')
    return conn

def create_users_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE,
                      password_hash TEXT)''')
    conn.commit()

def hash_password(password):
    # Create a salt and hash the password
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + password_hash  # Store salt with the hash

def verify_password(stored_password, provided_password):
    salt = stored_password[:16]  # Extract the salt from the stored hash
    stored_password_hash = stored_password[16:]  # Extract the hash
    provided_password_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return stored_password_hash == provided_password_hash  # Compare hashes

def user_exists(conn, username):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    return cursor.fetchone() is not None  # Returns True if user exists, else False


def register_user(conn, username, password):
        cursor = conn.cursor()
    
         # Generate a new salt
        salt = os.urandom(32)  # 32 bytes of random data for the salt
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

         # Combine the salt and the password hash for storage
        password_hash = salt + password_hash

        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, sqlite3.Binary(password_hash)))
        conn.commit()

        print(f"User '{username}' registered successfully.")
    


def login_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    
    if user is None:
        print("Username not found.")
        return False
    
    stored_password_hash = user[0]

    # Extract the salt from the stored password hash
    salt = stored_password_hash[:32]  # The first 32 bytes are the salt
    stored_password_hash = stored_password_hash[32:]  # The rest is the actual hash

    # Hash the provided password using the extracted salt
    provided_password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

 # Compare the provided password hash with the stored hash
    if provided_password_hash == stored_password_hash:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Incorrect password.")
        return False

def main():
    conn = create_connection()
    create_users_table(conn)

    username = input("Enter your username: ")

    if user_exists(conn, username):
        print("User found. Please log in.")
        password = input("Enter your password: ")
        if login_user(conn, username, password):
            print("Login successful!")
            # Proceed with the rest of the application
        else:
            print("Login failed. Please try again.")
    else:
        print("No account found with that username. Please register.")
        password = input("Create a password: ")
        register_user(conn, username, password)
        print("You can now log in.")
        # Optionally, you can directly log in after registration
        password = input("Enter your password to log in: ")
        if login_user(conn, username, password):
            print("Login successful!")
            # Proceed with the rest of the application
        else:
            print("Login failed. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()