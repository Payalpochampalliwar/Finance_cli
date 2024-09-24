import shutil
import sqlite3

def backup_database(backup_file):
    conn = sqlite3.connect('finance_app.db')
    with open(backup_file, 'wb') as f:
        for line in conn.iterdump():
            f.write(f'{line}\n'.encode('utf-8'))
    conn.close()
    print(f"Backup created: {backup_file}")

if __name__ == "__main__":
    backup_database('finance_backup.db')
