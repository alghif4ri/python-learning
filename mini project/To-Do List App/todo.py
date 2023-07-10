import sys
import function

def main():
    if not function.os.path.exists("tasks.txt"):
        open("tasks.txt", "w").close()

    while True:
        print("\Menu: ")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Clear All Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            function.show_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            function.add_task(task)
        elif choice == "3":
            task_number = int(input("Enter the task number to remove : "))
            function.remove_task(task_number)
        elif choice == "4":
            function.clear_tasks()
        elif choice == "5":
            sys.exit()
        else:
            print("Menu not exist!")
if __name__ == "__main__":
    main()
