import os
os.system('cls' if os.name == 'nt' else 'clear')

# Assignment manipulates references
x = 100
y = x 
print(y)
x = x + 1
print(y)
print(x)

a = [1, 2, 3] # 'a' now references the list [1, 2, 3]
print(a)
b = a
print("b:" , b)
a.append(4) # this changes the list 'a' references
print("b:" , b)