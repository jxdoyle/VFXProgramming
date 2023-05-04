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
    
    # animate cube
    cube = bpy.context.active_object
    cube.location = (7.61,0,0)
    cube.keyframe_insert(data_path = "location", frame = 70)
    cube.location = (35.54,0,0) 
    cube.keyframe_insert(data_path = "location", frame = 240)


    # Add a light
    light_data = bpy.data.lights.new(name="Light", type='AREA')
    light_object = bpy.data.objects.new(name="Light - Background", object_data=light_data)
    light_data.energy = 6000 # 6000 Watts
    light_data.size = 11.8

    console("ENDS:")

except Exception as e:
    console(e)