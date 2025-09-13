todos = []
while True: 
    user_action= input("Type add or show or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()
    match user_action:
        case 'add': 
            todo = input("Enter a task: ")
            todos.append(todo)
        case 'show' | 'display':
            i = 1
            for item in todos: 
                item = item.title()
                print(f"{i}. {item}")
                i = i+1
        case 'exit': 
            print("Bye Bye....")
            break
        case _: 
            print("Hey, you entered an unknown command!")