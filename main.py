from src.TaskManager import TaskManager

manager = TaskManager()

def main_menu():
    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Add task")
        print("2. Show all tasks")
        print("3. Find task")
        print("4. Filter by priority")
        print("5. Delete task")
        print("0. Exit")

        choice = input("Choose option: ").strip()

        match choice:
            case "1":
                print("Add task selected")
                manager.addTask()
            case "2":
                print("Show all tasks selected")
                manager.see_task()
            case "3":
                print("Find task selected")
                manager.task_finder()
            case "4":
                print("Filter by priority selected")
                manager.filterby_priority()
            case "5":
                print("Delete task selected")
                manager.remove_task()
            case "0":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice, try again")
main_menu()
