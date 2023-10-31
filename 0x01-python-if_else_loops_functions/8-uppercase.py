#!/usr/bin/python3
def uppercase(s):
    """Print a string in uppercase followed by a new line."""
    result = ""
    for char in s:
        result += chr(ord(char) - 32) if 'a' <= char <= 'z' else char
    print("{}".format(result))
