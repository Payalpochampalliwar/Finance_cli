import sqlite3

def restore_database(backup_file):
    conn = sqlite3.connect('finance_app.db')
    c = conn.cursor()

    # Drop existing tables if they exist
    c.execute('DROP TABLE IF EXISTS users')
    c.execute('DROP TABLE IF EXISTS transactions')
    c.execute('DROP TABLE IF EXISTS budgets')

    # Restore the database from the backup file
    with open(backup_file, 'r') as f:
        sql_script = f.read()
        conn.executescript(sql_script)
    
    conn.close()
    print(f"Database restored from: {backup_file}")

if __name__ == "__main__":
    restore_database('finance_backup.db')

