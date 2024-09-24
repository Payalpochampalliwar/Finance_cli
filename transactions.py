#Transaction Management

import sqlite3

def add_transaction(conn, user_id, amount, category, description, type_, date):
    c = conn.cursor()

    # Insert a new transaction
    c.execute('''
    INSERT INTO transactions (user_id, amount, description, category, type, date)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, amount, description, category, type_, date))

    conn.commit()
    print("Transaction added successfully.")

def view_transactions(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    
    print("\nID | Type    | Amount  | Category  | Description       | Date")
    print("------------------------------------------------------------")
    for row in rows:
        print(f"{row[0]:<3} | {row[1]:<7} | {row[2]:<7} | {row[3]:<8} | {row[4]:<15} | {row[5]}")
    print("")

def update_transaction(conn):
    transaction_id = input("Enter the ID of the transaction to update: ")
    
    # Handle the amount update
    amount_input = input("Enter new amount (or press Enter to keep current): ")
    amount = float(amount_input) if amount_input else None  # Only convert if input is provided

    # Handle the category update
    category = input("Enter new category (or press Enter to keep current): ") or None

    # Handle the description update
    description = input("Enter new description (or press Enter to keep current): ") or None

    # Handle the date update
    date = input("Enter new date (YYYY-MM-DD) (or press Enter to keep current): ") or None

    # Update the transaction in the database
    update_transaction(conn, transaction_id, amount=amount, category=category, description=description, date=date)

def delete_transaction(conn, transaction_id):
    c = conn.cursor()

    # Delete the transaction
    c.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))

    conn.commit()
import sqlite3


