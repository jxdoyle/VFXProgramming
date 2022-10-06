import os
os.system('cls' if os.name == 'nt' else 'clear')

# Best practice
def square(x):
    if x < 0:
        raise ValueError("only positive numbers are allowed")
    return x ** 2

try:
    square(-2)
except ValueError as error:
    print(error)


# Not best practice
x = 5
if  x == 2:
    print("x == 2") 
elif x == 3:
    print("x == 3")
else:
    print("x equals something else")
    print(x)
print("Outside 'if'")

assert(x > 5), f"Expected > 5 got {x}"


