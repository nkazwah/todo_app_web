FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """ Read text file
        and return list"""
    with open(filepath , "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def get_todos_no_lf(filepath = FILEPATH):
    """ Read text file
        and return list"""
    with open(filepath , "r") as file_local:
        todos_local = file_local.readlines()
    todos_local = [item.rstrip("\n") for item in todos_local]
    return todos_local

def write_todos(todos_arg , filepath = FILEPATH):
    """ Write text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())