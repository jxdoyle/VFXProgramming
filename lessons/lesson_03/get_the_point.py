# Class Point

from itertools import count


class Point:
    count = 0 # Class Variable

    def __init__(self, x, y):
        Point.count += 1
        self.x = x
        self.y = y
    
    def translate(self, x, y):
        self.x += x
        self.y += y

    # Overides default return string
    def __str__(self):
        result = f"x :{self.x} y :{self.y} count :{Point.count}"
        return result

    # Checks if two instances are equal (compare two objects)
    def __eq__(self, object):
        result = (self.x == object.x) and (self.y == object.y)
        return result

    def class_instance_function(self):
        print(f"x :{self.x} y :{self.y} Instance count :{Point.count}")

    def static_class_function():
        print(f"Class count :{Point.count}")

# Instance of Point
p1 = Point(1, 1)
p1.translate(2, 3)

p1.class_instance_function()
Point.static_class_function()

p2 = Point(3, 4)

# Are the Points Equal
print(p1 == p2)

print(p1 is p2)

# Print Coordinated
print(p1.x)
print(p1.y) 
print(p1)

# Add point to List
my_list = [p1]

# Append a point to the list
my_list.append(Point(3, 2))

# Print the list
print(my_list)

for object in my_list:
    print(object)

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
