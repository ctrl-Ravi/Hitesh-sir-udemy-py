"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task  
2. View Tasks  
3. Mark Task as Completed  
4. Delete Task  
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""








import os
TASK_FILE = "tasks.txt"
def load_tasks():
    tasks= []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, 'r', encoding="utf-8") as f:
            for line in f:
               text, status=  line.strip().rsplit("||", 1 ) # rsplit means split from right side
               tasks.append({"text": text, "done": status == "done"})
    return tasks


def save_tasks(tasks):
    with open(TASK_FILE, "w",encoding="utf-8") as file:
      for task in tasks:
         status = "done" if task["done"] else "not_done"
         file.write(f"{task['text']}||{status}\n")

def display_tasks(tasks):
    if not tasks:
        print(f"no tasks found")
    else:
        for i, task in enumerate(tasks, 1):
            checkbox= "✔️" if task["done"] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()


def task_manager():
    tasks= load_tasks()

    while True:
        print("\n -------- Task List Manager --------")
        print("1. Add task")
        print("2. View Task")
        print("3. Mark Task as complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5) ").strip()

        match choice:
            case "1":
                text = input("Enter Your Task: ").strip()
                if text:
                    tasks.append({"text":text, "done": False})
                    save_tasks(tasks)
                else:
                  print("Task Cannot be empty")
            case "2":
                display_tasks(tasks)
            case "3":
                display_tasks(tasks)
                try:
                    num =int(input("Enter Task number: "))
                    if 1<=num<=len(tasks):
                        if not tasks[num-1]["done"]:
                           tasks[num-1]["done"]= True
                           save_tasks(tasks)
                           print("Task Marked as done")
                           display_tasks(tasks)
                        else:
                            print("Task Already Marks As completed")
                            display_tasks(tasks)
                    else:
                         print("invalid Task number")
                except ValueError:
                     print("please Enter a number")
            case "4":
                display_tasks(tasks)
                try:
                    num =int(input("Enter Task number to delete: "))
                    if 1<=num<=len(tasks):
                        removed = tasks.pop(num-1)
                        save_tasks(tasks)
                        print(f"task removed:- {removed['text']}")
                    else:
                         print("invalid Task number")
                except ValueError:
                     print("please Enter a number")
            case "5":
                print("Exiting task manger")
                break
            case _: # this underscore means except all the cases input get then print
                print("please choose a valid option ")


task_manager()