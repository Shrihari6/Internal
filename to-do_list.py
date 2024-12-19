# To-Do List App

#19-12-2024
todo_list = []

def display_menu():
    print("\nTo-Do List App")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")


def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            status = "✓" if task['completed'] else "✗"
            print(f"{i}. {task['task']} [{status}]")


def add_task():
    task_name = input("\nEnter the task you want to add: ")
    todo_list.append({"task": task_name, "completed": False})
    print(f"Task '{task_name}' added to the list!")


def mark_completed():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]['completed'] = True
            print(f"Task '{todo_list[task_num - 1]['task']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


def delete_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted from the list!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\nExiting the To-Do List App. Have a productive day!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
