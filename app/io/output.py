

def write_in_console(some_text):
    """
    Write texts to console.

    Examples:
        >>> write_in_console("some_text")
        some_text

    Args:
        some_text(str): The text which need to write in console

    Return:
        None
    """
    print(some_text)
    return None

def write_in_file_with_python(some_text, file_name):
    """
    Writes text to a file using python's built-in capabilities.

    Examples:
        >>> write_in_file_with_python("some_text", "name_of_some_file.txt")
        Text written to file successfully!

    Args:
        some_text(str): The text which need to write in file
        file_name(str): The name of the file to which the text should be written

    Return:
        str: Text written to file successfully!
    """
    with open(file_name, 'w') as file:
        file.write(some_text)
    return "Text written to file successfully!"
