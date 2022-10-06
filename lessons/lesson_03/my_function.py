import os
os.system('cls' if os.name == 'nt' else 'clear')

# def <name>(arg1, arg2, ..., argN):​
#   <statements> return <value>​

def multiply(x, y):
    print("Function Argument x")
    print(hex(id(x)))
    x = x * y
    print("Local to function x")
    print(hex(id(x)))
    return x

x = 2
y = 10

print("Variables Passed by Assignment")
print(hex(id(x)))
print(multiply(x, y))
print("After Function Call")
print(hex(id(x)))