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
    collection.name = "Shapes"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    # Add primitive cube
    # bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))

    # Cube shape diagram for reference
    #
    #		  (-1.0, +1.0, +1.0)          (+1.0, +1.0, +1.0)
    #		          [5]                          [6]
    #		          #-----------------------------#
    #		         /|                            /|
    #		        / |                           / |
    #	  (-1.0, +1.0, -1.0)           (+1.0, +1.0, -1.0)
    #		  [1] /                         [2] /
    #		     #-----------------------------#    |
    #		     |    |                        |    |
    #		     |    |                        |    |
    #		     |   [4]                       |   [7]
    #		  (-1.0, -1.0, +1.0)         (+1.0, -1.0, +1.0)
    #		     |    #-----------------------------#
    #		     |   /                         |   /
    #		     |  /                          |  /
    #		     | /                           | /
    #		     |/                            |/
    #		     #-----------------------------#
    #		    [0]                           [3]
    #	(-1.0, -1.0, -1.0)         (+1.0, -1.0, -1.0)

    # Pyramid shape vertices
    vertices = [
            # Shape base
            ( -1.0, -1.0, 0 ), # [0] Vertex 1
            ( -1.0, +1.0, 0 ), # [1] Vertex 2
            ( +1.0, +1.0, 0 ), # [2] Vertex 3
            ( +1.0, -1.0, 0 ), # [3] Vertex 4

            # Pyramid "point"
            ( 0, 0, +1.0 ), # [4] Vertex 5
    ]

    # Define faces (index of vertices above)
    faces = [
            (0, 1, 2, 3),   # Bottom Face
            (0, 4, 1),      # Left Face
            (1, 4, 2),      # Back Face
            (2, 4, 3),      # Right Face
            (3, 4, 0),      # Front Face
    ]

    edges = [
        # we will define Edges later
    ]

    # Create mesh
    mesh_data = bpy.data.meshes.new("Pyramid")
    mesh_data.from_pydata(vertices, edges, faces)
    
    # Object using the mesh data
    object = bpy.data.objects.new("Pyramid", mesh_data)

    # Link the Object in the Scene
    bpy.context.collection.objects.link(object)

    # Add object to collection
    # object.location = (0, 0, 0)


    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Setup variables
    x = 1
    y = 1
    rows = 10
    columns = 10

    # Select shapes
    for obj in bpy.context.scene.objects:
                if obj.type == 'MESH':
                    obj.select_set(True)

    # Duplicate shapes into a row
    while y < rows:
        bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(0, 2, 0)})
        y += 1
    
    # Select entire row
    for obj in bpy.context.scene.objects:
                if obj.type == 'MESH':
                    obj.select_set(True)

    # Duplicate the row into columns
    while y == rows and x < columns:
        bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(-2, 0, 0)})
        x += 1

    # Create array
    shapes = bpy.data.collections["Shapes"].objects
    offset = 0

    # Add offset animations
    for i in shapes:
        i.scale = [0,0,0]
        i.keyframe_insert(data_path = "scale", frame = 1 + offset)
        i.scale = [1,1,5]
        i.keyframe_insert(data_path = "scale", frame = 50 + offset)
        i.scale = [1,1,.5]
        i.keyframe_insert(data_path = "scale", frame = 70 + offset)
        i.scale = [1,1,1]
        i.keyframe_insert(data_path = "scale", frame = 80 + offset)
        offset += 1

    # Save the blender file
    # Uncomment if you wish to automatically save
    # bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)

    console("ENDS:")

except Exception as e:
    console(e)