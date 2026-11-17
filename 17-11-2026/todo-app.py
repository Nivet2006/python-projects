class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        if name:
            self.tasks.append({"name": name, "done": False})
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return

        for number, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Not done"
            print(f"{number}. {task['name']} - {status}")

    def complete_task(self, number):
        if 1 <= number <= len(self.tasks):
            self.tasks[number - 1]["done"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")


class ConsoleTodoApp(Todo):
    def run(self):
        while True:
            print("\n--- TODO APP ---")
            print("1. Add task")
            print("2. View tasks")
            print("3. Complete task")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter a task: ").strip()
                self.add_task(name)
            elif choice == "2":
                self.show_tasks()
            elif choice == "3":
                print("\nSelect a task from below to mark as complete:")
                self.show_tasks()
                try:
                    number = int(input("Enter task number: "))
                    self.complete_task(number)
                except ValueError:
                    print("Please enter a number.")
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")

ConsoleTodoApp().run()
