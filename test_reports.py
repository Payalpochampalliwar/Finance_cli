import unittest
import sqlite3
from generate_reports import generate_monthly_report, generate_yearly_report

class TestReports(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute('''
            CREATE TABLE transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                type TEXT,
                amount REAL,
                category TEXT,
                description TEXT,
                date TEXT
            )
        ''')
        # Add sample data
        self.conn.execute("INSERT INTO transactions (user_id, type, amount, category, description, date) VALUES (1, 'Income', 2000.0, 'Salary', 'Monthly salary', '2024-09-01')")
        self.conn.execute("INSERT INTO transactions (user_id, type, amount, category, description, date) VALUES (1, 'Expense', 500.0, 'Rent', 'Monthly rent', '2024-09-03')")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_generate_monthly_report(self):
        report = generate_monthly_report(self.conn, "09", "2024")
        self.assertIn("Total Income: $2000.0", report)
        self.assertIn("Total Expenses: $500.0", report)

    def test_generate_yearly_report(self):
        report = generate_yearly_report(self.conn, "2024")
        self.assertIn("Total Income: $2000.0", report)
        self.assertIn("Total Expenses: $500.0", report)

if __name__ == '__main__':
    unittest.main()
