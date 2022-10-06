import os
os.system('cls' if os.name == 'nt' else 'clear')

x = 4
y = x
print(hex(id(x)))
print(hex(id(y)))
x = 5 # 'x' has a new memory address
y = x
print(hex(id(x)))
print(hex(id(y)))