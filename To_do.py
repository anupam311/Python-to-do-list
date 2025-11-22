def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")


print("Welcome to To-Do List App")

tasks = []

while True:
    show_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")
    
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(tasks, start=1):
                status = "Done" if task["done"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")
    
    elif choice == "3":
        task_num = int(input("Enter task number to delete: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    
    elif choice == "4":
        task_num = int(input("Enter task number to mark as done: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    
    elif choice == "5":
        print("Exiting the To-Do List App. Goodbye!")
        break

    