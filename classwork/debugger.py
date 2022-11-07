import bpy
import os
import sys
import importlib
import random

present_working_directory = os.path.dirname(bpy.data.filepath)

if not present_working_directory in sys.path:
    sys.path.append(present_working_directory)

import console_blender
importlib.reload(console_blender)
from console_blender import *
print(present_working_directory)

console(present_working_directory)

result = bpy.data.collections
console(f"Collection Name: {result}")

for obj in result:
    console(f"Collection Name: {obj.name}")

# add custom collection, rename it
collection = bpy.data.collections.new('Custom Collection')  
collection.name = "Scripted Objects"

# add collection to the scene
bpy.context.scene.collection.children.link(collection)

# set the new collection as the active one
layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
bpy.context.view_layer.active_layer_collection = layer_collection

# add shapes
bpy.ops.mesh.primitive_cylinder_add()
bpy.ops.mesh.primitive_circle_add()
bpy.ops.mesh.primitive_cone_add()
bpy.ops.mesh.primitive_monkey_add()
bpy.ops.mesh.primitive_cube_add()

# modify shapes
for result in bpy.data.collections:
    if result.name == collection.name:
        for object in result.objects:
            object.location.z += random.randint(1,3) # translate
            object.scale = (random.random(), random.random(), random.random()) # scale
            object.rotation_euler = (random.random(), random.random(), random.random()) # rotation
            console(f"x:{object.location.x}, y:{object.location.y}, z:{object.location.z}")