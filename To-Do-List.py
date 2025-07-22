tasks = []

def ToDoList(user_input, task):
    if not task:
        print("Task cannot be empty.")
        return
    if user_input == "add":
       tasks.append(task)
       print(f"Task '{task}' added to the list.")
    elif user_input == "remove" and task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print("Task not found or invalid command.")
        
while True:
    user_input = input("""
Please write if you want to add or remove tasks from your to do list."
if you are done simply write 'exit'
if you want to view the tasks already there then write 'view'""").strip().lower()
    if user_input == "exit":
        print("Current tasks in your To-Do List:")
        for task in tasks:
                print(f"- {task}")
        break
    
    elif user_input == "view":
        if tasks:
            print("Current tasks in your To-Do List:")
            for task in tasks:
                print(f"- {task}")
        else:
            print("Your To-Do List is empty.")
    elif user_input not in ["add", "remove"]:
        print("Invalid command. Please type 'add' or 'remove'.")
        continue
    
    elif user_input == "add":
        task = input("Write the task you want to add").strip()
        ToDoList(user_input, task)
    elif user_input == "remove":
        task = input("Write the task you want to remove").strip()
        ToDoList(user_input, task)
    else:
        print("Invalid command. Please type 'add' or 'remove'.")