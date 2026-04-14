import json
from json import JSONDecodeError
from src.Task import Task

class TaskManager:
    def __init__(self):
        try:
            with open("data.json", "r") as f:
                self.tasklist = json.load(f)
        except (FileNotFoundError, JSONDecodeError) as e:
            print(e)
            self.tasklist = []

            with open("data.json", "w") as file:
                json.dump(self.tasklist, file)
            print("File Created")


    def addTask(self):
        title = input("Give a name: ")
        descrition = input("Give a description: ")
        priority = input("Give a priority: ")

        tk = Task(title, descrition, priority)

        self.tasklist.append(tk.to_dict())
        self.save_data()

    def see_task(self):
        for task in self.tasklist:
            print(task["title"], task["description"], task["priority"])


    def save_data(self):
        with open("data.json", "w") as file:
                json.dump(self.tasklist, file, indent=4)


    def remove_task(self):
        delete = input("Del: ")
        for title in self.tasklist:
            if title['title'].lower() == delete:
                self.tasklist.remove(title)
                print("Task Ended")

        self.save_data()

    def filterby_priority(self):
        ft = input("Filter by priority: ").lower()
        found = False

        for task in self.tasklist:
            if task["priority"].lower() == ft:
                print(task["title"], task["description"], task["priority"])
                found = True

        if not found:
            print("No tasks or such priority found")

    def task_finder(self):
        tf = input("Task Find: ")
        found = False
        for task in self.tasklist:
            if tf.lower() in task['title'].lower():
                found = True
                print(task["title"], task["description"], task["priority"])
        if not found:
            print("Task not found")


