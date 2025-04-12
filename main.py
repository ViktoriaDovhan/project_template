from app.io.input import *
from app.io.output import *


def main():
    text_from_console = read_from_console()
    text_from_file_with_python = read_from_file_with_python("some_file_with_text.txt")
    text_from_file_with_pandas = read_from_file_with_pandas("some_file_with_text.txt")

    write_in_console("Text from console: " + text_from_console)
    write_in_console("Text from file with python capabilities: " + text_from_file_with_python)
    write_in_console("Text from file with pandas capabilities: " + text_from_file_with_pandas)

    all_texts_together = (
    "Text from console: " + text_from_console
    + "\nText from file with python capabilities: " + text_from_file_with_python
    + "\nText from file with pandas capabilities: " + text_from_file_with_pandas
    )
    write_in_file_with_python(all_texts_together, "some_file_for_texts.txt")


if __name__ == "__main__":
    main()
