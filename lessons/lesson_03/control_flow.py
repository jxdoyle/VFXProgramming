import os
os.system('cls' if os.name == 'nt' else 'clear')


#if Statement
print("'if' Statement")
x = 5
if  x == 2:
    print("x == 2") 
elif x == 3:
    print("x == 3")
else:
    print("x equals something else")
    print(x)
print("Outside 'if'")
print(os.linesep)

#Nested if statement
print("Nested 'if' Statement")
x = 42

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
    if x == 42:
        print("42!!! The meaning of life!")
  else:
    print("but not above 20.") 
print(os.linesep)

# While statement
print("'while' Statement")
x = 0
while x  < 10:
    print("Inside While Loop")
    x = x + 1
    print(f"Incremented x inside While Loop x:{x}")
    if x == 7:
        print(f"x == {x}")
        break
print("Outside of the Do While loop")
print(os.linesep)

# Do While (modification of While) statement
print("'do while' Statement")
x = 0
while True:
    print("Inside Do While Loop")
    x = x + 1
    print(f"Incremented x inside Do While Loop x:{x}")
    if x == 1:
        print(f"x == {x}")
        break
    if x == 2:
        print(f"x == {x}")
        break
print("Outside of the Do While loop")
print(os.linesep)

# for loop
print("'for' loop")
x = 1
for	x in range(10):
    x = x + 1
    print(f"x == {x}")
    print("Inside For Loop")
    if	x == 9:
        print("x == 9")
        break
print("Outside of the for loop")
print(os.linesep)