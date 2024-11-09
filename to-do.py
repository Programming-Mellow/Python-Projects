def add_item(lst, value):
    lst.append("☐ " + value)
    print("Successfully added item!")

def view_list(lst):
    print("\nTo-Do List:")
    for i in lst:
        print(i)

def clear_list(lst):
    lst.clear()

def remove_item(lst, value):
    for i in range(len(lst)):
        if (str(lst[i][2:]).lower() == str(value).lower()):
            del lst[i]
            print("Successfully removed item!")
            return
    print("Item not found; please try again!")

def check_item(lst, value):
    for i in range(len(lst)):
        item = lst[i]
        if item.startswith("☐ "):
            clean_item = item[2:]
            if str(clean_item).lower() == str(value).lower():
                lst[i] = "☑ " + clean_item
                print("Successfully checked item!")
                return
        elif item.startswith("☑ "):
            continue
    print("Item not found; please try again!")

def uncheck_item(lst, value):
    for i in range(len(lst)):
        item = lst[i]
        if item.startswith("☑ "):
            clean_item = item[2:]
            if str(clean_item).lower() == str(value).lower():
                lst[i] = "☐ " + clean_item
                print("Successfully unchecked item!")
                return
        elif item.startswith("☐ "):
            continue
    print("Item not found; please try again!")

def edit_item(lst, old_val, new_val):
    for i in range(len(lst)):
        cmpare = lst[i][2:]
        if str(cmpare).lower() == str(old_val).lower():
            if lst[i].startswith("☐ "):
                lst[i] = "☐ " + new_val
                print("\nSuccessfully edited item!")
            elif lst[i].startswith("☑ "):
                lst[i] = "☑ " + new_val
                print("\nSuccessfully edited item!")
            return
    print("Item not found; try again!")

def load(filename, lst):
    try:
        with open(filename, "r") as fp:
            for entry in fp:
                add_item(lst, entry)
    except FileNotFoundError:
        print("\nFile not found! Try again.\n")

def save(filename, lst):
    try:
        with open(filename, "w") as fp:
            for entry in lst:
                fp.write(entry + "\n")
    except FileNotFoundError:
        print("\nFile not found! Try again.\n")


def print_commands():
    print("\nAvailable Commands:\n\nView the list\n- view\nThis will generate a viewable task list of what is currently on the list.\n\nClear the list\n- clear\nThis will clear all tasks off the list and allow you to start a new list with a blank slate.\n\nAdding a task\n- add [task]\nThis will add a task onto the list.\n\nRemoving a task\n- remove [task]\nThis will remove the task from the list.\n\nCheck a task\n- check [task]\nThis will input a checkmark into the box to mark the task as checked off.\n\nUncheck a task\n- uncheck [task]\nThis will uncheck the selected task if it has been checked before.\n\nEdit an item\n- edit [oldtask], [newtask]\nThis will edit the original task [oldtask] with the new task [newtask].\n\nLoad To-Do List\n - load (filename)\nThis will load your to-do list into the program\n\nSave To-Do List\n - save\nThis will save the current entries into the filename you've loaded.\n\nExit program\n- exit\nThis will terminate the program.\n")


if __name__ == "__main__":
    todo_list = []
    new_file = False
    while True:
        todo_file = input("Please input your filename that you will load into the program or indicate that you are creating a new one:\n\n Available Commands:\n\n-load [filename]\nLoad a pre-existing to-do list\n\n-new\nCreate a new to-do list.\n\n")
        split_todofile = todo_file.split(" ", 1)
        if (split_todofile[0].lower() == "load"):
            load(split_todofile[1], todo_list)
        elif (split_todofile[0].lower() == "new"):
            new_file = True
            break
        else:
            print("Invalid command, please try again!")

    print("Simple To-do List")
    print_commands()

    while True:
        command = input("\nPlease input your choice:\n")
        cmd_split = command.split(" ", 1)
        if (cmd_split[0].lower() == "cmd" or cmd_split[0].lower() == "cmds"):
            print_commands()
        elif (cmd_split[0].lower() == "add"):
            add_item(todo_list, cmd_split[1])
        elif (cmd_split[0].lower() == "remove"):
            remove_item(todo_list, cmd_split[1])
        elif (cmd_split[0].lower() == "check"):
            check_item(todo_list, cmd_split[1])
        elif (cmd_split[0].lower() == "uncheck"):
            uncheck_item(todo_list, command[8:])
        elif (cmd_split[0].lower() == "edit"):
            if len(cmd_split) < 2:
                print("Please provide both the old task and the new task.")
            else:
                old_new = cmd_split[1].split(", ")
                if len(old_new) != 2:
                    print("Please provide both the old task and the new task separated by a comma and a space.")
                else:
                    edit_item(todo_list, old_new[0], old_new[1])
        elif (cmd_split[0].lower() == "clear"):
            clear_list(todo_list)
        elif (cmd_split[0].lower() == "view"):
            view_list(todo_list)
        elif (cmd_split[0].lower() == "load"):
            load(cmd_split[1], todo_list)
        elif(cmd_split[0].lower() == "save" and new_file):
            save("todo_list.txt", todo_list)
        elif (cmd_split[0].lower() == "save" and not new_file):
            save(cmd_split[1], todo_list)
        elif (cmd_split[0].lower() == "exit"):
            print("Goodbye!\n\n")
            break
        else:
            print("Unknown command; please try again!\n\n")