import functions
import PySimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to do", key="todo")
add_button = sg.Button("Add")
list_todos = sg.Listbox(values=functions.get_todos(),
                        key="todos",
                        enable_events=True,
                        size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_todos, edit_button]],
                   font=("Helvetica", 20))


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_to_file(todos)
            list_todos.update(todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_to_file(todos)
            list_todos.update(todos)
        case "todos":
            input_box.update(values["todos"][0].strip())
        case sg.WINDOW_CLOSED:
            break

window.close()
