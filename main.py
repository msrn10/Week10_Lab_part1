import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, description):
    priority = input("Enter priority (low, medium, high) [default: medium]: ").strip().lower()
    if priority not in ["low", "medium", "high"]:
        priority = "medium"
    

    task = {
        "description": description,
        "completed": False,
        "priority": priority
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task saved successfully")

def list_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{i+1}. {task['description']} [{status}] - Priority: {task['priority']}")





def complete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid task number")
        return
    tasks[index]["completed"] = True
    save_tasks(tasks)
    print("Task marked as complete")

def delete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid task number")
        return
    tasks.pop(index)
    save_tasks(tasks)
    print("Task deleted")

## new commands here ##

def count(tasks):
    total = len(tasks)
    print(f"Total tasks: {total}")




def main():
    tasks = load_tasks()

    while True:
        command = input("\nEnter command (add/list/complete/delete/count/exit): ").strip().lower()

        if command == "add":
            desc = input("Enter task description: ")
            add_task(tasks, desc)

        elif command == "list":
            list_tasks(tasks)

        elif command == "complete":
            num = int(input("Enter task number: ")) - 1
            complete_task(tasks, num)

        elif command == "delete":
            num = int(input("Enter task number: ")) - 1
            delete_task(tasks, num)

        elif command == "count":
            count(tasks)
        

        elif command == "exit":
            print("Goodbye")
            break

        else:
            print("Invalid command")

if __name__ == "__main__":
    main()