import os
os.system('cls' if os.name == 'nt' else 'clear')


#if Statement
x = 5
if  x == 2:
    print("x == 2") 
elif x == 3:
    print("x == 3")
else:
    print("x equals something else")
    print(x)
print("Outside 'if'")

#Nested if statement
x = 42

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
    if x == 42:
        print("42!!! The meaning of life!")
  else:
    print("but not above 20.") 