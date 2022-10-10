# create cube class
class Cube:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

# create empty location list 
locations_list = []

# iniilise x, y, x, at 0 for loop later
x = 0
y = 0
z = 0

# number of cubes to make
index = 10    

# fill location list array with cubes
# x increases by 1 on each loop, '*' multiplier spaces out the cubes
for x in range(index):
  locations_list.append(Cube(3*x, y, z))

# print the x, y, z coordinates from the location list array
for object in locations_list:
  print(f"{object.x}, {object.y}, {object.z}")

# line break to make the array print outs more readable
print("\n")

# modify the y value of a cube
locations_list[3] = (Cube(9, 3, z)) 

# print the x, y, z coordinates from the ammended location list array
for object in locations_list:
  print(f"{object.x}, {object.y}, {object.z}")

# line break to make the array print outs more readable
print("\n")

# delete a cube from the location list array
locations_list.pop(7)

# print the x, y, z coordinates from the ammended location list array
for object in locations_list:
  print(f"{object.x}, {object.y}, {object.z}")