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

# Function that inserts new tasks into database
def add_task(task_name, due_date):
    conn = sqlite3.connect('mulenga_tasks.db')
    c.execute('''INSERT INTO tasks (task_name, due_date, status) VALUES (?, ?, ?)''', (task_name, due_date, 'Pending'))
    conn.commit()
    conn.close()

# Function that updates the task status    
def update_task_status(task_id, status):
    conn = sqlite3.connect('mulenga_tasks.db')
    c.execute('''UPDATE tasks SET status = ? WHERE id = ?''', (status, task_id))
    conn.commit()
    conn.close()

# Function to delete a task
def delete_task(task_id):
    conn = sqlite3.connect('mulenga_tasks.db')
    c = conn.cursor()
    c.execute('''DELETE FROM tasks WHERE id = ?''', (task_id))
    conn.commit()
    conn.close()