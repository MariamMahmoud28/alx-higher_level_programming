#!/usr/bin/python3
if __name__ == "__main":
    """import all hidden directories"""
    import hidden_4

    for name in dir(hidden_4):
        if not name.startswith("__"):
             print(name)
