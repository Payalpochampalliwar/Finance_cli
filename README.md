**Finance CLI Application**
A command-line-based personal finance manager to manage and track income, expenses, and generate reports. Built using Python and SQLite, this application allows users to add, view, update, delete transactions, and generate monthly or yearly financial reports.

**Table of Contents**
Features
Setup
Usage
Commands
Database Schema
Testing
Contributing
License
**Features**
Add Transaction: Record income and expense transactions.
View Transactions: Display all transactions.
Update Transaction: Modify existing transaction details.
Delete Transaction: Remove a transaction from the database.
Generate Reports: Generate monthly and yearly financial reports summarizing income, expenses, and savings.
**Setup**
**Prerequisites**
Python 3.x
SQLite3 (or any SQL DBMS that SQLite supports)
**Installation**
**Clone the repository:**

git clone https://github.com/your-username/finance-cli.git
cd finance-cli
**Install required Python packages (if any):**

pip install -r requirements.txt

**Set up the SQLite database**:
python db.py

**Run the application:**
python main.py

**Usage**
Once the application is running, you will be prompted with a menu to manage your transactions and generate reports.

**Example:**
**To add a transaction:**
Select option 1, then enter the details as prompted (amount, type, description, etc.).
**To generate a monthly report:**
Select option 3 and provide the month and year.
**Commands**
Add Transaction: Adds a new transaction for the user.
View Transactions: Displays all recorded transactions.
Update Transaction: Updates specific fields of a transaction.
Delete Transaction: Removes a transaction by ID.
Generate Monthly Report: Generates a report of income and expenses for a given month.
Generate Yearly Report: Generates a report of income and expenses for a given year.
**Database Schema**
The application uses a SQLite database to store transaction data.

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    category TEXT,
    description TEXT,
    type TEXT,  -- 'Income' or 'Expense'
    date TEXT   -- Format: YYYY-MM-DD
);
**Testing**
To run tests for this application:

Ensure you have unittest installed (default in Python).
2.Run the test suite:
python test_reports.py
python test_transactions.py
This will run the unit tests for the transaction and report generation functionality.

**Contributing**
Feel free to open issues and submit pull requests if you'd like to contribute to this project.

1.Fork the repository.
2.Create a new branch.
3.Make your changes.
4.Submit a pull request.
**License**
This project is licensed under the MIT License.

