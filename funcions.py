FILEPATH = "todos.txt"


def get_todos(local_filepath = FILEPATH):
    """
    Read the todos items from todos.txt
    :param local_filepath:
    :return: list of todos items
    """
    with open(local_filepath, 'r') as local_file:
        local = local_file.readlines()
        return local


def write_todos(todos_arg, local_filepath = FILEPATH):
    """
    write the todos items in a text file
    :param todos_arg:
    :param local_filepath:
    :return: none
    """
    with open(local_filepath, 'w') as local_file:
        local = local_file.writelines(todos_arg)

