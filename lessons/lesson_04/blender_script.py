import random                       # Math Random
import bpy                          # Blender Python Module
import os                           # Operating System Module
import sys                          # System Module
import importlib                    # Importing Modules Module

# Find out root directory of Blender Project
directory = os.path.dirname(bpy.data.filepath)
if not directory in sys.path:       # Check if this directory is in system Path
    sys.path.append(directory)      # Add Directory to Discoverable Path

import console_blender              # Import Custom Write to Console
importlib.reload(console_blender)   # Add custom module to the Blender Project (now that directory is know)
from console_blender import *       # After a reload import all the functions of the custom module

console("STARTS:")

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

# Add custom collection, rename it and add it as a scene child
collection = bpy.data.collections.new('Custom Collection')
collection.name = "Scripted Objects"

# Add the Collection to the Scene
bpy.context.scene.collection.children.link(collection)

# Set the new collection as the active one
layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
bpy.context.view_layer.active_layer_collection = layer_collection

for i in range(3):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    # Add objects to Collection
    obj = bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
    
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)

    # Add objects to Collection
    obj = bpy.ops.mesh.primitive_cylinder_add(location=(x, y, z))    

    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    r = random.randint(1, 3)
    # Add objects to Collection
    obj = bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=(x, y, z))

console("Accessing Data-Blocks")
console("Accessing Scene Collection")
result = bpy.data.objects
console(f"Objects in the Scene: {result}")

console("Accessing Collections in a Scene")

for result in bpy.data.collections:
    if result.name == collection.name:
        for object in result.objects:
            object.location.z += random.randint(1, 3) # Translate
            object.scale = (random.random(), random.random(), random.random()) # Scale
            object.rotation_euler = (random.random(), random.random(), random.random()) # Rotation
            console(f"x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")

console("ENDS:")