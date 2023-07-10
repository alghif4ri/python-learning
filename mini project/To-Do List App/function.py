import os

def show_tasks():
    #mencari file tasks yang ada
    if not os.path.exists("tasks.txt"):
        print("No tasks found!")
        return

    #jika ada buka file
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    # menampilkan tasks
    if tasks:
        print("Tasks: ")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")
    else:
        print("No tasks found!")


def add_task(task):
    #menambahkan task baru ke dalam file
    with open("tasks.txt","a") as file:
        file.write(task+"\n")
    print("Task added successfully!")


def remove_task(task_number):
    #mencari task yang ada didalam file tasks.txt
    if not os.path.exists("tasks.txt"):
        print("No tasks found!")
        return
    
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    #hapus spesifik task
    if task_number <= len(tasks):
        del tasks[task_number - 1]

        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task number! Please enter a valid one.")


def clear_tasks():
    #mencari file tasks.txt
    if os.path.exists("tasks.txt"):
        #hapus file tasks.txt
        os.remove("tasks.txt")
        print("All tasks cleared!")
    else:
        print("No tasks found!")
