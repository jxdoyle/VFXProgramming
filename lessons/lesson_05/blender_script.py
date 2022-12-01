import random                       # Math Random
import bpy                          # Blender Python Module
import os                           # Operating System Module
import sys                          # System Module
import importlib                    # Importing Modules Module
from math import pi, radians        # Transformations Rotation

# Find out root directory of Blender Project
directory = os.path.dirname(bpy.data.filepath)
if not directory in sys.path:       # Check if this directory is in system Path
    sys.path.append(directory)      # Add Directory to Discoverable Path

import console_blender              # Import Custom Write to Console
importlib.reload(console_blender)   # Add custom module to the Blender Project (now that directory is know)
from console_blender import *       # After a reload import all the functions of the custom module

console("STARTS:")

# Catch any errors
try:    
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

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    # Setup frame increment
    frames = 0
    frame_increment = 5
    offset = 10 # makes each object look a bit more dynamic

    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                # Starting Location
                frames = frame_increment
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")

                frames += frame_increment
                object.location = (random.randint(1, 10), random.randint(1, 3), random.randint(1, 3)) # Translate
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")

                frames += frame_increment
                object.rotation_euler = (random.random(), random.random(), random.random()) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")

                frames += frame_increment
                object.rotation_euler = (radian_rotation, radian_rotation, radian_rotation) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")

                frames += frame_increment
                object.rotation_euler = (radians(30), radians(30), radians(30)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += frame_increment
                object.scale = (random.random(), random.random(), random.random()) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")

                frames += frame_increment
                object.scale = (random.random(), random.random(), random.random()) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")

                frames += frame_increment
                object.scale = (random.random(), random.random(), random.random()) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")

                frames += frame_increment
                object.scale = (random.random(), random.random(), random.random()) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")

                offset += 1

    # Save the blender file
    # Uncomment if you wish to automatically save
    # bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)

    console("ENDS:")

except Exception as e:
    console(e)