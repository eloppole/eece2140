# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:03:53 2025

@author: conno
"""

# To-Do List Program
tasks = []  # List to store tasks

def add_task():
    task = input("Enter the new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    print("\nTo-Do List:")
    for task in tasks:
        status = "Done" if task["completed"] else "Not Done"
        print(f"{task['task']} [{status}]")
    print()

def mark_completed():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            print(f"Task '{tasks[task_number]['task']}' marked as completed\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task():
    """Delete a task from the list."""
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"Task '{removed_task['task']}' deleted successfully\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def first():
    while True:
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")
#==============================================================================
# Main function to invoke the two functions
def main():
    print("Executing Question 1:")
    first() # Call the function for Question 1
#==============================================================================
# Invoke the main function
if __name__ == "__main__":
    main()
#==============================================================================
