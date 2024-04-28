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
    c = conn.cursor()
    c.execute('''INSERT INTO tasks (task_name, due_date, status) VALUES (?, ?, ?)''', (task_name, due_date, 'Pending'))
    conn.commit()
    conn.close()
    

# Function that updates the task status    
def update_task_status(task_id, status):
    conn = sqlite3.connect('mulenga_tasks.db')
    c = conn.cursor()
    c.execute('''UPDATE tasks SET status = ? WHERE id = ?''', (status, task_id))
    conn.commit()
    conn.close()
    

# Function to delete a task
def delete_task(task_id):
    conn = sqlite3.connect('mulenga_tasks.db')
    c = conn.cursor()
    c.execute('''DELETE FROM tasks WHERE id = ?''', (task_id,))
    conn.commit()
    conn.close()
    

# Function to get tasks
def get_tasks():
    conn = sqlite3.connect('mulenga_tasks.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM tasks''')
    tasks = c.fetchall()
    conn.close()
    return tasks

# Function to populate tasks in the database
def populate_tasks():
    tasks_to_insert = [
        ("Task 1", "2024-05-01"),
        ("Task 2", "2024-05-03"),
        ("Task 3", "2024-05-05")
    ]
    try:
        conn = sqlite3.connect('mulenga_tasks.db')
        c = conn.cursor()
        c.executemany('''INSERT INTO tasks (task_name, due_date, status) VALUES (?, ?, ?)''', [(name, date, 'Pending') for name, date in tasks_to_insert])
        conn.commit()
        print("Tasks succesfully inserted into the  database.")
    except sqlite3.Error as e:
        print(f"Error inserting tasks: {e}")
    finally:
        conn.close()

populate_tasks()
    
# Function to view tasks
def  view_tasks():
    try:
        conn = sqlite3.connect('mulenga_tasks.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM tasks''')
        tasks =  c.fetchall()
        if tasks:
            print("Tasks in the database:")
            for task in tasks:
                print(f"ID: {task[0]}, Task Name: {task[1]}, Due Date: {task[2]}, Status: {task[3]}")
            else:
                print("No tasks found in the database.")
    except sqlite3.Error as e:
        print(f"Error accessing tasks: {e}")
    finally:
        conn.close()

view_tasks()
