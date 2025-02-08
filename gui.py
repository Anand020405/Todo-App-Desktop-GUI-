import function
import FreeSimpleGUI as sg
import time

sg.theme("Black")

label_time = sg.Text("", key = 'Time')

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key = 'todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values = function.get_todos(), 
                      key = 'todos_list',
                      enable_events = True,
                      size = [45,10])
Edit_button = sg.Button("Edit")
Complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App", 
                layout= [[label_time],
                         [label],
                         [input_box, add_button],
                         [list_box, Edit_button],
                         [exit_button, Complete_button]],
                font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED:
        break

    if values['todos_list'] != [] and values['todos_list'] != previous_value:
        window['todo'].update(value=values['todos_list'][0].strip("\n"))
    previous_value = values['todos_list']

    if event == 'Add':
        if values['todo'].strip() != '':
            todos = function.get_todos()
            new_todo = values['todo']+'\n'
            todos.append(new_todo)
            function.send_todos(todos)
            window['todos_list'].update(values=[x.strip("\n") for x in todos])

    elif event == 'Edit':
        if values['todos_list'] != []:
            todo_to_edit = values['todos_list'][0]
            new_todo = values['todo']
            todos = function.get_todos()
            edit_index = todos.index(todo_to_edit)
            todos[edit_index] = new_todo + '\n'
            function.send_todos(todos)
            window['todos_list'].update(values=todos)
            continue
        sg.popup("Please select a To-Do to edit")
            

    elif event == "Complete":
        if values['todos_list'] != []:
            todos = function.get_todos()
            todo_completed = values['todos_list'][0]
            todos.remove(todo_completed)
            function.send_todos(todos)
            window['todos_list'].update(values=todos)
            window['todo'].update(value="")
            continue
        sg.popup("Please select a To-Do to complete")

    elif event == 'Exit':
        break

    window['Time'].update(time.strftime("%b %d, %Y %H:%M:%S"))



window.close()
