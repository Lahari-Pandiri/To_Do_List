# todo_list.py

import os

# File to store tasks
FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n========== TO-DO LIST ==========")
    print("1️⃣  Add Task")
    print("2️⃣  View Tasks")
    print("3️⃣  Remove Task")
    print("4️⃣  Mark Task as Done")
    print("5️⃣  Quit")
    print("================================")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            task = input("Enter task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print(f"✅ Task '{task}' added!")
            else:
                print("⚠️ Task cannot be empty!")

        elif choice == '2':
            if tasks:
                print("\n📝 Your Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("\n😴 No tasks yet!")

        elif choice == '3':
            if tasks:
                print("\nSelect a task number to remove:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Enter task number: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        save_tasks(tasks)
                        print(f"🗑️ Task '{removed}' removed.")
                    else:
                        print("❌ Invalid task number!")
                except ValueError:
                    print("⚠️ Please enter a valid number.")
            else:
                print("😅 Nothing to remove!")

        elif choice == '4':
            if tasks:
                print("\nSelect a task to mark as done:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Enter task number: "))
                    if 1 <= num <= len(tasks):
                        tasks[num - 1] += " ✅ (Done)"
                        save_tasks(tasks)
                        print("🎉 Task marked as done!")
                    else:
                        print("❌ Invalid task number!")
                except ValueError:
                    print("⚠️ Please enter a valid number.")
            else:
                print("😅 Nothing to mark!")

        elif choice == '5':
            print("👋 Goodbye! Tasks saved.")
            break

        else:
            print("❌ Invalid choice. Please enter 1–5.")

if __name__ == "__main__":
    main()
