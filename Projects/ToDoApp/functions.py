FILEPATH = "todos.txt"


def write_to_file(content, file_name=FILEPATH):
    """ Write the to-do items list in the text file"""
    with open(file_name, "w") as file:
        file.writelines(content)


def get_todos(file_name=FILEPATH):
    """ Read a text file and return the list of to-do items."""
    with open(file_name, "r") as file:
        return file.readlines()
