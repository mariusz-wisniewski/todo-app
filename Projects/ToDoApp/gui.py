import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

FONT_TYPE_SIZE = ("Helvetica", 20)

clock_label = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to do", key="todo")
add_button = sg.Button("Add")
list_todos = sg.Listbox(values=functions.get_todos(),
                        key="todos",
                        enable_events=True,
                        size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock_label],
                           [label],
                           [input_box, add_button],
                           [list_todos, edit_button, complete_button],
                           [exit_button]],
                   font=FONT_TYPE_SIZE)


while True:
    event, values = window.read(timeout=1000)
    clock_label.update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_to_file(todos)
            list_todos.update(todos)
        case "Edit":
            try:
                todos = functions.get_todos()
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_to_file(todos)
                list_todos.update(todos)
            except IndexError:
                sg.Popup("Please select an item first.", font=FONT_TYPE_SIZE)
        case "Complete":
            try:
                todos = functions.get_todos()
                todo_co_complete = values["todos"][0]
                todos.remove(todo_co_complete)
                functions.write_to_file(todos)
                list_todos.update(todos)
                input_box.update(value="")
            except IndexError:
                sg.Popup("Please select an item first.", font=FONT_TYPE_SIZE)
        case "Exit":
            break
        case "todos":
            input_box.update(values["todos"][0].strip())
        case sg.WINDOW_CLOSED:
            break

window.close()
