#!/usr/bin/python3

import sys

if __name__ == "__main__":
    # Get all command-line arguments, excluding the script name (sys.argv[0])
    args = sys.argv[1:]

    # Initialize a variable to store the sum
    total = 0

    # Loop through the arguments, cast each to an integer, and add to the total
    for arg in args:
        total += int(arg)

    # Print the total sum
    print(total)

