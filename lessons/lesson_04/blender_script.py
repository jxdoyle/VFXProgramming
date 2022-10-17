import random
import bpy
import os
import sys
import importlib

os.system('cls' if os.name == 'nt' else 'clear')

directory = os.path.dirname(bpy.data.filepath)
if not directory in sys.path:
    sys.path.append(directory)

import console_blender

importlib.reload(console_blender)

from console_blender import *

for i in range(3):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
    
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    bpy.ops.mesh.primitive_cylinder_add(location=(x, y, z))

    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    r = random.randint(1, 3)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=(x, y, z))

console("Accessing Data-Blocks")
result = bpy.data.objects
console(f"Objects in the Scene: {result}")

console("Accessing Collections")
result = list(bpy.data.objects)
for record in result:
    console(f"Object: {record}")

for record in result:
    object = record.location
    console(f"x:{object.x}, y:{object.y}, x:{object.z}")

for record in result:
    record.location.z += random.randint(1, 3) # Translate
    record.scale = (random.random(), random.random(), random.random()) # Scale
    record.rotation_euler = (random.random(), random.random(), random.random()) # Rotation
    console(f"x:{object.x}, y:{object.y}, x:{object.z}")

console("Accessing Scenes")
result = bpy.data.scenes
console(f"Scenes: {result}")

for object in result:
    console(f"Scene Name: {object.collection.name}")

console("Accessing Collections")
result = bpy.data.collections
console(f"Collections: {result}")

for object in result:
    console(f"Collection Name: {object.name}")

console("Accessing Materials")
result = bpy.data.materials
console(f"Scenes: {result}")

collection = bpy.data.collections.new('Custom Collection')
collection.name = "Scripted Objects"

#bpy.data.scenes.collection.children






