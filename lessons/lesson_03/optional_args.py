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

x = 2
y = 10

print("Variables Passed by Assignment")
print(hex(id(x)))
print(multiply(x, y))
print("After Function Call")
print(hex(id(x)))

print(hex(id(x)))
print(multiply(x, y, 20, 40))
print("After Function Call")
print(hex(id(x)))