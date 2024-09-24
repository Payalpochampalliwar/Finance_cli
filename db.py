#Database Management

import sqlite3
from sqlite3 import Error

def create_connection(db_file="finance_app.db"):
    """Create a database connection to an SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database '{db_file}' successfully.")
    except Error as e:
        print(e)
    return conn

def create_tables(conn):
    """Create tables for users, transactions, and budgets if they don't exist."""
    try:
        cursor = conn.cursor()

        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        # Create transactions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                type TEXT,
                amount REAL,
                category TEXT,
                description TEXT,
                date TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # Create budgets table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT UNIQUE,
                amount REAL
            )
        ''')

        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

def drop_tables(conn):
    """Drop all tables (for development purposes)."""
    try:
        cursor = conn.cursor()

        cursor.execute('DROP TABLE IF EXISTS users')
        cursor.execute('DROP TABLE IF EXISTS transactions')
        cursor.execute('DROP TABLE IF EXISTS budgets')

        conn.commit()
        print("Tables dropped successfully.")
    except Error as e:
        print(f"Error dropping tables: {e}")

def close_connection(conn):
    """Close the database connection."""
    if conn:
        conn.close()
        print("Database connection closed.")
