import sqlite3
from db import create_connection, create_tables, close_connection
from transactions import add_transaction, view_transactions, update_transaction, delete_transaction

def main():
    # Connect to the database
    conn = create_connection()
    create_tables(conn)  # Ensure the tables are created if not already
    
    print("Welcome to Personal Finance Manager!\n")
    
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Update Transaction")
        print("5. Delete Transaction")
        print("6. Exit")
        
        option = input("\nSelect an option: ")
        
        if option == '1':
            add_income(conn)
        elif option == '2':
            add_expense(conn)
        elif option == '3':
            view_transactions(conn)
        elif option == '4':
            update_transaction_prompt(conn)
        elif option == '5':
            delete_transaction_prompt(conn)
        elif option == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
    
    conn.close()

def add_income(conn):
    user_id = int(input("Enter user ID: "))
    amount = float(input("Enter amount: "))
    category = "Income"
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD): ")
    
    add_transaction(conn, user_id, amount, category, description, "Income", date)
    print(f"Income of ${amount} for '{description}' added on {date}.")

def add_expense(conn):
    user_id = int(input("Enter user ID: "))
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., Food, Rent): ")
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD): ")
    
    add_transaction(conn, user_id, amount, category, description, "Expense", date)
    print(f"Expense of ${amount} for '{description}' added under '{category}' on {date}.")

def update_transaction_prompt(conn):
    transaction_id = int(input("Enter the ID of the transaction to update: "))
    amount = float(input("Enter new amount (or press Enter to keep current): ") or None)
    category = input("Enter new category (or press Enter to keep current): ")
    description = input("Enter new description (or press Enter to keep current): ")
    date = input("Enter new date (YYYY-MM-DD) (or press Enter to keep current): ")
    
    update_transaction(conn, transaction_id, amount, category, description, date)
    print(f"Transaction ID {transaction_id} has been updated.")

def delete_transaction_prompt(conn):
    transaction_id = int(input("Enter the ID of the transaction to delete: "))
    delete_transaction(conn, transaction_id)
    print(f"Transaction ID {transaction_id} has been deleted.")

    close_connection(conn)

if __name__ == "__main__":
    main()
