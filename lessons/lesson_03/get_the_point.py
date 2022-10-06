# Class Point

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Instance of Point
p1 = Point(1, 1)

# Print Coordinated
print(p1.x)
print(p1.y) 

# Add point to List
my_list = [p1]

# Append a point to the list
my_list.append(Point(3, 2))

# Print the list
print(my_list)

# Print the Point Coordinates
print("Objects with int str")
for object in my_list:
    print("x:" + str(object.x) + " y:"+ str(object.y))

# Add a point to list
def add_point(listing, point):
    listing.append(point)

# Call add a point to list
add_point(my_list, Point(4, 5))

# Print the Point Coordinates
print("Objects with formatting")
for object in my_list:
    print("x:{x_coordinate} y:{y_coordinate}".format(x_coordinate=object.x, y_coordinate=object.y))

# Copy list (Points)
new_list = my_list[:]

# Print the Point Coordinates
print("Objects with cleaner formatting")
for object in new_list:
    print(f"x:{object.x} y:{object.y}")
