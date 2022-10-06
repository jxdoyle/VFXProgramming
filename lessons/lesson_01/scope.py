import sys
import os
os.system('cls' if os.name == 'nt' else 'clear')

x = 500
print('x:', x)
print('x address global : ', hex(id(x)))
print('x references global scope : ', sys.getrefcount(x))

def custom_function():
  x = 300
  print('x:', x)
  print('x references function scope : ', sys.getrefcount(x))
  print('x address function scope : ', hex(id(x)))
  y = 100
  print('y:', y)
  print('y address function scope : ', hex(id(y)))
  print('y references function scope : ', sys.getrefcount(y))

custom_function()

print('x:', x) 
print('x address global scope : ', hex(id(x)))
print('x references global scope : ', sys.getrefcount(x))
y = 300
print('y:', y) 
print('y address local scope : ', hex(id(y)))
print('y references local scope : ', sys.getrefcount(y))

s = "awesome"

def myfunc():
  s = "fantastic"
  print("Python is " + s)

myfunc()

print("Python is " + s)