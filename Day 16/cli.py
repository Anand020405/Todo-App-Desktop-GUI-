from function import get_todos, send_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)
run = True
while run:
    user_action = input("Type add, show, edit, complete or end: ")
    user_action =  user_action.lower().strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todos = get_todos()
        user_todo = user_action[4:] + "\n"
        todos.append(user_todo)
        send_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index,item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}. {item.title()}")

    elif user_action.startswith("edit"):
        todos = get_todos()
        try:
            number = int(user_action[5:])
            new_todo = input("Enter the new item: ") + "\n"
            todos[number-1] = new_todo
        except ValueError:
            print("The edit command expects the serial number and not a text")
        except IndexError:
            print("The given serial number was not found")
        send_todos(todos)

    elif user_action.startswith("complete"):
        todos = get_todos()
        try:
            number = int(user_action[9:])
            print(f"Todo {todos.pop(number-1).strip("\n")} was removed from the list")
        except ValueError:
            print("The complete command expects the serial number and not a text")
        except IndexError:
            print("The given serial number was not found")
        send_todos(todos)

    elif user_action.startswith("end"):
        run = False

    else:
        print("Hey, that command was not recognised")

print("Bye")