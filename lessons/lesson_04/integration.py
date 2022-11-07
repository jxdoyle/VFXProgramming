# This script allows us to integrate scripts external to Blender
# We do not have to reload every time we make a change in the source script using VSC

import bpy                          # Blender Python Module
import os                           # Operating System Module
import sys                          # System Module
import importlib                    # Importing Modules Module

# Find out root directory of Blender Project
directory = os.path.dirname(bpy.data.filepath)
if not directory in sys.path:       # Check if this directory is in system Path
    sys.path.append(directory)      # Add Directory to Discoverable Path

import blender_script              # Import Blender Script
importlib.reload(blender_script)   # Add Blender Script to the Blender Project (now that directory is know)
from blender_script import *       # After a reload import all the functions of the Blender Script