import sqlite3

# Connect to your SQLite database
def connect_to_db(db_name):
    return sqlite3.connect(db_name)

# List all tables in the database
def list_tables(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [table[0] for table in tables]

# View the schema of a specific table
def view_schema(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    schema = cursor.fetchall()
    return schema

# Query and print data from a specific table
def query_table_data(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    return rows

# Main function to demonstrate usage
def main():
    db_name = 'finance_app.db'  # Replace with your database file name
    conn = connect_to_db(db_name)
    
    # List all tables
    tables = list_tables(conn)
    print("Tables:")
    for table in tables:
        print(f" - {table}")

    # View schema of each table
    for table in tables:
        print(f"\nSchema for table {table}:")
        schema = view_schema(conn, table)
        for column in schema:
            print(column)
    
    # Query data from each table
    for table in tables:
        print(f"\nData from table {table}:")
        rows = query_table_data(conn, table)
        for row in rows:
            print(row)
    
    conn.close()

if __name__ == "__main__":
    main()
