import sqlite3

# Connect to the database
conn = sqlite3.connect('finance_app.db')

# Create the transactions table if it doesn't exist
conn.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        type TEXT,
        amount REAL,
        category TEXT,
        description TEXT,
        date TEXT
    )
''')


def generate_monthly_report(conn, month, year):
    cursor = conn.cursor()

    cursor.execute('''SELECT SUM(amount) FROM transactions 
                      WHERE type = 'Income' AND strftime('%m', date) = ? AND strftime('%Y', date) = ?''',
                   (month, year))
    total_income = cursor.fetchone()[0] or 0

    cursor.execute('''SELECT SUM(amount) FROM transactions 
                      WHERE type = 'Expense' AND strftime('%m', date) = ? AND strftime('%Y', date) = ?''',
                   (month, year))
    total_expenses = cursor.fetchone()[0] or 0

    total_savings = total_income - total_expenses

    report = f"--- Monthly Financial Report: {month}-{year} ---\n"
    report += f"Total Income: ${total_income:.2f}\n"
    report += f"Total Expenses: ${total_expenses:.2f}\n"
    report += f"Total Savings: ${total_savings:.2f}\n"

    cursor.execute('''SELECT category, SUM(amount) FROM transactions 
                      WHERE type = 'Expense' AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
                      GROUP BY category''',
                   (month, year))
    rows = cursor.fetchall()
   
    for row in rows:
        report += f"{row[0]:<15}: ${row[1]:.2f}\n"

    if total_income > 0:
        savings_rate = (total_savings / total_income) * 100
        report += f"\nYou have saved {savings_rate:.2f}% of your income this month.\n"
    else:
        report += "\nNo income recorded for this month.\n"

    return report


def generate_yearly_report(conn, year):
    cursor = conn.cursor()

    cursor.execute('''SELECT SUM(amount) FROM transactions 
                      WHERE type = 'Income' AND strftime('%Y', date) = ?''', 
                   (year,))
    total_income = cursor.fetchone()[0] or 0

    cursor.execute('''SELECT SUM(amount) FROM transactions 
                      WHERE type = 'Expense' AND strftime('%Y', date) = ?''', 
                   (year,))
    total_expenses = cursor.fetchone()[0] or 0

    total_savings = total_income - total_expenses
    
    report = f"--- Yearly Financial Report: {year} ---\n"
    report += f"Total Income: ${total_income:.2f}\n"
    report += f"Total Expenses: ${total_expenses:.2f}\n"
    report += f"Total Savings: ${total_savings:.2f}\n"
    
    average_income = total_income / 12
    average_expenses = total_expenses / 12
    average_savings = total_savings / 12
    
    report += f"\nAverage Monthly Income: ${average_income:.2f}\n"
    report += f"Average Monthly Expenses: ${average_expenses:.2f}\n"
    report += f"Average Monthly Savings: ${average_savings:.2f}\n"

    cursor.execute('''SELECT strftime('%m', date) as month, SUM(amount) FROM transactions 
                      WHERE type = 'Expense' AND strftime('%Y', date) = ? 
                      GROUP BY month ORDER BY SUM(amount) DESC''', 
                   (year,))
    rows = cursor.fetchall()

    if rows:
        highest_spending_month = rows[0] 
        lowest_spending_month = rows[-1] 

        report += f"\nHighest Spending Month: {highest_spending_month[0]} - ${highest_spending_month[1]:.2f}\n"
        report += f"Lowest Spending Month: {lowest_spending_month[0]} - ${lowest_spending_month[1]:.2f}\n"
    
    if total_income > 0:
        savings_rate = (total_savings / total_income) * 100
        report += f"\nYear-End Savings Rate: {savings_rate:.2f}%"
    else:
        report += "\nNo income recorded for this year."
    return report

if __name__ == "__main__":
    conn = sqlite3.connect('finance_app.db')
    generate_monthly_report(conn, '09', '2024')
    print("\n")
    generate_yearly_report(conn, '2024')
    conn.close()


