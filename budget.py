import sqlite3

def set_budget(conn):
    category = input("Enter category (e.g., Food, Rent): ")
    amount = float(input("Enter budget amount: "))
    
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO budgets (category, amount)
        VALUES (?, ?)
        ON CONFLICT(category) 
        DO UPDATE SET amount=excluded.amount
    ''', (category, amount))
    conn.commit()
    
    print(f"Budget of ${amount:.2f} set for '{category}'.")

def view_budgets(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM budgets")
    rows = cursor.fetchall()
    
    print("\nID | Category | Amount")
    print("-------------------------")
    for row in rows:
        print(f"{row[0]:<3} | {row[1]:<8} | ${row[2]:.2f}")
    print("")

def check_budget_status(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT category, amount FROM budgets")
    budgets = cursor.fetchall()

    for category, budget_amount in budgets:
        cursor.execute('''
            SELECT IFNULL(SUM(amount), 0) FROM transactions
            WHERE category = ? AND type = 'Expense'
        ''', (category,))
        total_expense = cursor.fetchone()[0]

        print(f"{category}: Budget ${budget_amount:.2f} | Spent ${total_expense:.2f} | Remaining ${budget_amount - total_expense:.2f}")


def main():
    conn = sqlite3.connect('finance_app.db')
    
    
    while True:
        print("\n1. Set Budget")
        print("2. View Budgets")
        print("3. Check Budget Status")
        print("4. Exit")
        
        option = input("\nSelect an option: ")
        
        if option == '1':
            set_budget(conn)
        elif option == '2':
            view_budgets(conn)
        elif option == '3':
            check_budget_status(conn)
        elif option == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
    
    conn.close()

if __name__ == "__main__":
    main()

