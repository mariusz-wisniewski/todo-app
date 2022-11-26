import functions
import time


FILE_NAME = "todos.txt"

current_time = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {current_time}")

while True:
    user_action: str = input("Type add, show, edit or complete: ").strip()

    if user_action.startswith("add "):
        todos = functions.read_file()
        todos.append(user_action.removeprefix("add").strip() + "\n")
        functions.write_to_file(todos)
    elif user_action == "show":
        todos = functions.read_file()
        for index, todo in enumerate(todos):
            print(f"{index + 1} - {todo.strip()}")
    elif user_action.startswith("edit "):
        try:
            todos = functions.read_file()
            number = int(user_action.removeprefix("edit"))
            new_todo = input("Enter a new todo: ").strip() + "\n"
            todos[number-1] = new_todo
            functions.write_to_file(todos)
        except ValueError:
            print("Your command is not valid.")
    elif user_action.startswith("complete "):
        try:
            todos = functions.read_file()
            number = int(user_action.removeprefix("complete"))
            todo_to_remove = todos[number-1].strip()
            todos.pop(number - 1)
            functions.write_to_file(todos)
            print(f"Todo {todo_to_remove} was removed from the list")
        except IndexError:
            todos = functions.read_file()
            print(f"Index out of range. Please select index between 1 and {len(todos)}")
    elif user_action == "exit":
        break
    else:
        print("Unknown user action.")

print("We're done!")
