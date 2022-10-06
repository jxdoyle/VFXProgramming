
# Cube cordinate class
class Coordinate:
  def __init__(cube, x, y, z):
    cube.x = x
    cube.y = y
    cube.z = z

coords = Coordinate(1, 1, 1)
print(coords.x)
print(coords.y) 
print(coords.z) 

coords_list = [coords]

coords_list.append(Coordinate(3, 3, 3))
for object in coords_list:
    print("x:" + str(object.x) + " y:"+ str(object.y) + " z:"+ str(object.z))