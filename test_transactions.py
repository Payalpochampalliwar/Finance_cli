import unittest
import sqlite3
from transactions import add_transaction, update_transaction, view_transactions, delete_transaction

class TestTransactions(unittest.TestCase):

    def setUp(self):
        # Create a temporary in-memory database for testing
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
    
    def tearDown(self):
        # Close the connection after each test
        self.conn.close()

    def test_add_transaction(self):
        add_transaction(self.conn, 1, 100.0, "Food", "Grocery shopping", "Expense", "2024-09-04")
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0][4], "Food")
    
    def test_update_transaction(self):
        add_transaction(self.conn, 1, 100.0, "Food", "Grocery shopping", "Expense", "2024-09-04")
        update_transaction(self.conn, 1, amount=150.0)
        cursor = self.conn.cursor()
        cursor.execute("SELECT amount FROM transactions WHERE id=1")
        updated_amount = cursor.fetchone()[0]
        self.assertEqual(updated_amount, 150.0)

    def test_delete_transaction(self):
        add_transaction(self.conn, 1, 100.0, "Food", "Grocery shopping", "Expense", "2024-09-04")
        delete_transaction(self.conn, 1)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM transactions WHERE id=1")
        transaction = cursor.fetchone()
        self.assertIsNone(transaction)

if __name__ == '__main__':
    unittest.main()

