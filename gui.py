import function
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key = 'todo')
add_button = sg.Button("Add")

exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App", 
                layout= [[label], 
                            [input_box, add_button], 
                            [exit_button]],  
                font=('Helvetica', 20))

while True:
    event, values = window.read()
    if event == 'Add':
        
        todos = function.get_todos()
        new_todo = values['todo']+'\n'
        todos.append(new_todo)
        function.send_todos(todos)

    elif event == 'Exit':
        break

    elif event == sg.WIN_CLOSED:
        break

window.close()
