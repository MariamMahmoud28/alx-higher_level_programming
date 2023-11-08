#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
update_dictionary(my_dict, 'b', 42)  # Replaces the value for 'b' key
update_dictionary(my_dict, 'd', 99)  # Adds a new key 'd' with the value 99
print(my_dict)
