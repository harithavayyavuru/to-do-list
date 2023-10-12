import pickle

# Create an empty list to store tasks
tasks = []

# Function to display the menu
def display_menu():
    print("To-Do List Menu:")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Save tasks")
    print("6. Load tasks")
    print("7. Quit")

# Function to add a task
def add_task():
    task = input("Enter a task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

# Function to list tasks
def list_tasks():
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index}. {task['task']} - {status}")

# Function to mark a task as complete
def mark_task_as_complete():
    task_number = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["done"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        deleted_task = tasks.pop(task_number)
        print(f"Task '{deleted_task['task']}' deleted!")
    else:
        print("Invalid task number.")

# Function to save tasks to a file
def save_tasks():
    with open("tasks.pkl", "wb") as file:
        pickle.dump(tasks, file)
    print("Tasks saved!")

# Function to load tasks from a file
def load_tasks():
    global tasks
    try:
        with open("tasks.pkl", "rb") as file:
            tasks = pickle.load(file)
        print("Tasks loaded!")
    except FileNotFoundError:
        print("No saved tasks found.")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_task_as_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_tasks()
    elif choice == "6":
        load_tasks()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
