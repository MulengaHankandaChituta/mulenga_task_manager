# Python program to implement a simple task manager
# I will also demonstrate the use of a simple database
# The database in use will be sqlite3

import sqlite3

# Function to create a database
def create_database():
    conn = sqlite3.connect('mulenga_tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, task_name TEXT, due_date TEXT, status TEXT)''')
    conn.commit()
    conn.close()