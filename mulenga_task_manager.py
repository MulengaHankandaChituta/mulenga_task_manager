# Python program displaying a task manager
import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Pending"

def add_task(tasks, title, description, due_date):
    task = Task(title, description, due_date)
    tasks.append(task)
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.title} - Due: {task.due_date} - Status: {task.status}")

def update_task(tasks, index, title, description, due_date, status):
    if 1 <= index <= len(tasks):
        task = tasks[index - 1]
        task.title = title
        task.description = description
        task.due_date = due_date
        task.status = status
        print("Task updated successfully.")
    else:
        print("Invalid task index.")

def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task index.")

def main():
    tasks = []

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
            add_task(tasks, title, description, due_date)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            index = int(input("Enter the index of the task to update: "))
            title = input("Enter new task title: ")
            description = input("Enter new task description: ")
            due_date_str = input("Enter new due date (YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
            status = input("Enter new status: ")
            update_task(tasks, index, title, description, due_date, status)

        elif choice == "4":
            view_tasks(tasks)
            index = int(input("Enter the index of the task to delete: "))
            delete_task(tasks, index)

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()