import unittest
import sqlite3
from auth import register_user, login_user

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password_hash BLOB
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_register_user(self):
        username = 'testuser'
        password = 'password'
        
        # Call the function to register the user
        register_user(self.conn, username, password)
        
        # Verify that the user was registered successfully
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        self.assertIsNotNone(user)  # Assert that the user exists in the database

    def test_login_user(self):
        username = 'testuser'
        password = 'password'

        # Register the user
        register_user(self.conn, username, password)

        
        # Call the function to log in the user
        result = login_user(self.conn, username, password)
        
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()



