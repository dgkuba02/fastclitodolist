todo_list = []

def show_menu():
    print("=== TO-DO LIST ===")
    print("1. Add task.")
    print("2. Delete task.")
    print("3. Mark task.")
    print("4. Show tasks.")
    print("5. Exit.")
    
def add_task():
    task = input("Enter task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added.")
    
def view_tasks():
    if not todo_list:
        print("No tasks found.")
        return
    for i, item in enumerate(todo_list, 1):
        status = "✅" if item["done"] else "❌"
        print(f"{i}. [{status}] {item['task']}")

def complete_task():
    if not todo_list:
        print("No tasks to complete.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as complete: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["done"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

        
def delete_task():
    if not todo_list:
        print("No tasks to delete.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            view_tasks()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            
if __name__ == "__main__":
    main()