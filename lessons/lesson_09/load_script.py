# This script allows us to integrate scripts external to Blender
# We do not have to reload every time we make a change in the source script using VSC

import bpy                          # Blender Python Module
import os                           # Operating System Module
import sys                          # System Module

# Find out root directory of Blender Project and append the file to run
file = os.path.join(os.path.dirname(bpy.data.filepath), "blender_animation_script.py")
exec(compile(open(file).read(), file, 'exec'))