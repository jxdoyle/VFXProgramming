import os
os.system('cls' if os.name == 'nt' else 'clear')

# def <name>(arg1, arg2, ..., argN):​
#   <statements> return <value>​

def multiply(x, y, a = 10, b = 20):
    """Multiply the arguments and return result"""
    print("Function Argument x")
    print(hex(id(x)))
    x = x * y * a * b
    print("Local to function x")
    print(hex(id(x)))
    return x

# No Overloading
# def multiply(x, y, a = 10, b = 20, c = 50):
#    print("Function Argument x")
#    print(hex(id(x)))
#    x = x * y
#    print("Local to function x")
#    print(hex(id(x)))
#    return x

def no_return():
    """Does not return a value or result"""
    print("no return here")
    some_val = 42

x = 2
y = 10

def functional(x):
    """We can pass any variable or function to this function"""
    print("Whats my function ((⇀‸↼))")
    print("Lets call the function that was passed")
    print(x)
    print("Now I can see my purpose")

def list_maker(x):
    sample_list = ['one','two','three',1, 2, 3]
    sample_list.append(x)
    return sample_list

print("Variables Passed by Assignment")
print(hex(id(x)))
print(multiply(x, y))
#help(multiply) uncomment to get help on multiply method

print("After Function Call")
print(hex(id(x)))

print(hex(id(x)))
print(multiply(x, y, 20, 40))

print("After Function Call")
print(hex(id(x)))

print("No Return Value Specified: Prints 'None'")
print(no_return())

print("Functions can be passed")
def pass_function(fn, arg):
    print(fn(arg))

pass_function(float, 100)
pass_function(str, 100)

# Examples of functional programming
print(functional(no_return()))
print(functional(multiply(x, y)))

# Functions can return collections or types
print(functional(list_maker(x)))

# Order of arguments can be different
def printGamer(tag, points, location):
    print(f"Tag:{tag} Points:{points} Location:{location}")

printGamer(location="Some Game Room", tag="MuddyGames", points=100)

# Functions can return multiple values
def return_multiple_values(x = 0, y = 0, z = 0):
    """
    Code Document String: multi-line
    Used to explain how to use function to programmers
    We can return multiple values from a function
    Keyword  arguments:
    x -- x coordinate (default = 0)
    y -- y coordinate (default = 0)
    z -- z coordinate (default = 0)
    """
    x = 1
    y = 2
    z = 3
    return(x, y, z)

(a, b, c) = return_multiple_values()

print(f"a:{a} b:{b} c:{c}")

input("Press the 'q' key to exit help, press enter to continue")
# Press the 'q' key to exit help
help(return_multiple_values)