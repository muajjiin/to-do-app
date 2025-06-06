
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['task']}")


def add_task(tasks, task_text):
    tasks.append({"task": task_text, "done": False})
    print(f"Added task: {task_text}")


def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(f"Marked task #{index+1} done.")
    else:
        print("Invalid task number.")


def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted task: {removed['task']}")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nYour To-Do List:")
        list_tasks(tasks)
        print("\nCommands: add <task>, done <num>, delete <num>, quit")
        command = input("Enter command: ").strip()

        if command == "quit":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break

        elif command.startswith("add "):
            task_text = command[4:].strip()
            if task_text:
                add_task(tasks, task_text)
            else:
                print("Please provide a task to add.")

        elif command.startswith("done "):
            num_str = command[5:].strip()
            if num_str.isdigit():
                mark_done(tasks, int(num_str) - 1)
            else:
                print("Please provide a valid task number.")

        elif command.startswith("delete "):
            num_str = command[7:].strip()
            if num_str.isdigit():
                delete_task(tasks, int(num_str) - 1)
            else:
                print("Please provide a valid task number.")

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
