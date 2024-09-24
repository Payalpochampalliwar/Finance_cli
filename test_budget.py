import unittest
from unittest.mock import patch
import sqlite3
from budget import set_budget, view_budgets, check_budget_status

class TestBudget(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute('''
            CREATE TABLE budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT UNIQUE,
                amount REAL
            )
        ''')
        self.conn.execute('''
            CREATE TABLE transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                amount REAL,
                category TEXT,
                date TEXT
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_set_budget(self):
        inputs = ["Food", "200.0"]
        with patch('builtins.input', side_effect=inputs):
            set_budget(self.conn)
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM budgets WHERE category = 'Food'")
        budget = cursor.fetchone()
        self.assertIsNotNone(budget)
        self.assertEqual(budget[2], 200.0)

    def test_view_budgets(self):
        self.conn.execute("INSERT INTO budgets (category, amount) VALUES ('Food', 200.0)")
        self.conn.commit()
        
        with patch('builtins.print') as mock_print:
            view_budgets(self.conn)
        
        mock_print.assert_any_call("\nID | Category | Amount")
        mock_print.assert_any_call("-------------------------")
        mock_print.assert_any_call("1   | Food     | $200.00")

    def test_check_budget_status(self):
        self.conn.execute("INSERT INTO budgets (category, amount) VALUES ('Food', 200.0)")
        self.conn.execute("INSERT INTO transactions (type, amount, category, date) VALUES ('Expense', 50.0, 'Food', '2024-09-04')")
        self.conn.commit()
        
        with patch('builtins.print') as mock_print:
            check_budget_status(self.conn)
        
        mock_print.assert_any_call("Food: Budget $200.00 | Spent $50.00 | Remaining $150.00")

if __name__ == '__main__':
    unittest.main()


