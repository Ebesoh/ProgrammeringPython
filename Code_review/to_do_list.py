#Simple To-Do List Program

def show_menu():
    print("\nTo_Do List Menu")
    print("1.View tasks")
    print("2.Add task")
    print("3.Delete task")
    print("4.Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to do list is empty!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks,1):
            print(f"{i}.{task}")

def add_task(tasks):
    task = input("Enter a new task:")
    tasks.append(task)
    print(f'"{task}" added to the list.')

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the number of the task to delete:"))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num-1)
            print(f"{removed_task} removed from the list")
        else:
            print("Invalid task number")

def main():
    tasks =[]
    while True:
        show_menu()
        choice = input("Choose an option(1-4):")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")
if __name__ == "__main__":
    main()

