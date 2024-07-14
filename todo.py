todo_list = []

def show_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    todo_list.append(task)
    print(f'Task "{task}" added.')

def view_tasks():
    if not todo_list:
        print("No tasks available.")
    else:
        for idx, task in enumerate(todo_list):
            print(f"{idx + 1}. {task}")

def remove_task():
    view_tasks()
    if todo_list:
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(todo_list):
            removed_task = todo_list.pop(task_no - 1)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
