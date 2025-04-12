

def read_from_console():
    """
    Reads texts from console.

    Examples:
        input: some text
        >>> read_from_console()
        some text

    Return:
        some_text(str): Text that we read from console
    """
    some_text = input("Enter some text: ")
    print("The text read successfully!")
    return some_text


def read_from_file_with_python(file_name):
    """
    Reads from a file using python's built-in capabilities.

    Examples:
        >>> read_from_file_with_python("name_of_some_file.txt")
        text from file
    Args:
        file_name(str): The name of the file from which the text should be read

    Return:
        some_text(str): Text that we read from file
    """
    with open(file_name, 'r') as file:
        some_text = file.read()
    print("The text read successfully!")
    return some_text


def read_from_file_with_pandas(file_name):
    """
    Reads from a file using pandas's capabilities.

    Examples:
        >>> read_from_file_with_pandas("name_of_some_file.txt")
        text from file

    Args:
        file_name(str): The name of the file from which the text should be read

    Return:
        some_text(str): Text that we read from file
    """
    import pandas as pd
    with open(file_name, "r") as file:
        lines = file.readlines()
    series = pd.Series(lines)
    some_text = "\n".join(series.str.strip())
    print("The text read successfully!")
    return some_text
