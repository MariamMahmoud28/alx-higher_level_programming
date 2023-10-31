#!/usr/bin/python3

def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False

def uppercase(s):
    for c in s:
        print("{:c}".format(ord(c) if not islower(c) else ord(c) - 32), end="")
    print("")  # Move this line outside of the for loop

# Example usage:
uppercase("Hello, World!")

