#!/usr/bin/python3

import importlib.util

module_name = 'hidden_4'
module_spec = importlib.util.spec_from_file_location(module_name, 'hidden_4.pyc')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)

# Get the names defined in the module and filter them
filtered_names = [name for name in dir(module) if not name.startswith('__')]

# Sort the names in alphabetical order
filtered_names.sort()

# Print the names one per line
for name in filtered_names:
    print(name)

