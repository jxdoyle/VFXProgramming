# This is a comment
# Start comments with # – the rest of line is ignored

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Can include a “documentation string” as the first line of any
# new function or class that you define

def my_function(a, b):
    """this function adds two numbers"""
    res = a + b
    print(res)

my_function(2, 2)
