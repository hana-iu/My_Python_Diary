todos = []
while True: 
    user_action= input("Type add or show or exit: ")
    match user_action:
        case 'add': 
            todo = input("Enter a task: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit': 
            print("Bye Bye....")
            break