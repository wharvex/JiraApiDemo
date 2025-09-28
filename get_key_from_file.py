import os

def get_key_from_file(filename="key.txt"):
    """
    Looks for a file named 'key.txt' in the current directory,
    expects it to have a single line in the format: key=some_text_here,
    and returns 'some_text_here'. Raises FileNotFoundError if file doesn't exist,
    ValueError if the format is wrong.
    """
    filepath = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"{filename} not found in the current directory.")

    with open(filepath, "r") as f:
        line = f.readline().strip()
        if not line.startswith("key="):
            raise ValueError(f"The file should start with 'key=', got: {line}")
        return line[len("key="):]