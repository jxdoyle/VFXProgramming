import os
os.system('cls' if os.name == 'nt' else 'clear')

# def <name>(arg1, arg2, ..., argN):​
#   <statements> return <value>​

def multiply(x, y, a = 10, b = 20):
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
    print("no return here")
    some_val = 42

x = 2
y = 10

def functional(x):
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
print("After Function Call")
print(hex(id(x)))

print(hex(id(x)))
print(multiply(x, y, 20, 40))
print("After Function Call")
print(hex(id(x)))

print("No Return Value Specified: Prints 'None'")
print(no_return())

# Examples of functional programming
print(functional(no_return()))
print(functional(multiply(x, y)))

# Functions can return collections or types
print(functional(list_maker(x)))