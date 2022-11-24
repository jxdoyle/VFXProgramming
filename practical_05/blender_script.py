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

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('Custom Collection')
    collection.name = "Shapes"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    ### Pyramid
    # Shape vertices
    vertices = [
            # Shape base
            ( -1.0, -1.0, 0.0 ), # [0] Vertex 1
            ( -1.0, +1.0, 0.0 ), # [1] Vertex 2
            ( +1.0, +1.0, 0.0 ), # [2] Vertex 3
            ( +1.0, -1.0, 0.0 ), # [3] Vertex 4

            # Pyramid "point"
            ( 0.0,  0.0, +1.0 )  # [4] Vertex 5
    ]

    # Define faces (index of vertices above)
    faces = [
            ( 0, 1, 2, 3 ),   # Bottom
            ( 0, 4, 1 ),      # Left 
            ( 1, 4, 2 ),      # Back 
            ( 2, 4, 3 ),      # Right
            ( 3, 4, 0 )       # Front
    ]

    edges = [
        # we will define Edges later
    ]

    # Create mesh
    mesh_data = bpy.data.meshes.new("Pyramid")
    mesh_data.from_pydata(vertices, edges, faces)
    
    # Object using the mesh data
    object = bpy.data.objects.new("Pyramid", mesh_data)

    # Link the object in the scene
    bpy.context.collection.objects.link(object)

    # Set location centered in scene
    object.location = (0, 0, 0)

    ### Raised Hexagon
    # Shape vertices
    vertices = [
            # Bottom
            (  0.0, -1.0,  0.0 ), # [0] Vertex 1
            ( -1.0, -0.5,  0.0 ), # [1] Vertex 2    
            ( -1.0,  0.5,  0.0 ), # [2] Vertex 3    
            (  0.0, +1.0,  0.0 ), # [3] Vertex 4    
            ( +1.0, +0.5,  0.0 ), # [4] Vertex 5   
            ( +1.0, -0.5,  0.0 ), # [5] Vertex 6

            # Top
            (  0.0, -1.0, +1.0 ), # [6] Vertex 7
            ( -1.0, -0.5, +1.0 ), # [7] Vertex 8   
            ( -1.0, +0.5, +1.0 ), # [8] Vertex 9   
            (  0.0, +1.0, +1.0 ), # [9] Vertex 10   
            ( +1.0, +0.5, +1.0 ), # [10] Vertex 11  
            ( +1.0, -0.5, +1.0 )  # [11] Vertex 12
    ]

    # Define faces (index of vertices above)
    faces = [
            ( 0, 1, 2, 3, 4, 5),   # Bottom
            ( 0, 1, 7, 6 ),        # Front left
            ( 1, 2, 8, 7 ),        # Left
            ( 2, 3, 9, 8 ),        # Back left
            ( 3, 4, 10, 9 ),       # Back right
            ( 4, 5, 11, 10 ),      # Right
            ( 5, 0, 6, 11 ),       # Front right
            ( 6, 7, 8, 9, 10, 11 ) # Top
    ]

    edges = [
        # we will define Edges later
    ]

    # Create mesh
    mesh_data = bpy.data.meshes.new("Raised Hexagon")
    mesh_data.from_pydata(vertices, edges, faces)
    
    # Object using the mesh data
    object = bpy.data.objects.new("Raised Hexagon", mesh_data)

    # Link the object in the scene
    bpy.context.collection.objects.link(object)

    # Set location next to previous shape on Y axis
    object.location = (0, 2, 0)

    ### Raised Pyramid 
    # Shape vertices
    vertices = [
            # Shape base/cube
            ( -1.0, -1.0,  0.0 ), # [0] Vertex 1
            ( -1.0, +1.0,  0.0 ), # [1] Vertex 2
            ( +1.0, +1.0,  0.0 ), # [2] Vertex 3
            ( +1.0, -1.0,  0.0 ), # [3] Vertex 4
            ( -1.0, -1.0, +1.0 ), # [4] Vertex 1
            ( -1.0, +1.0, +1.0 ), # [5] Vertex 2
            ( +1.0, +1.0, +1.0 ), # [6] Vertex 3
            ( +1.0, -1.0, +1.0 ), # [7] Vertex 4

            # Pyramid "point"
            (  0.0,  0.0, +2.0 )  # [8] Vertex 5
    ]

    # Define faces (index of vertices above)
    faces = [
            # Lower points
            ( 0, 1, 2, 3 ),   # Bottom 
            ( 0, 1, 5, 4 ),   # Left 
            ( 1, 2, 6, 5 ),   # Back 
            ( 2, 3, 7, 6 ),   # Right 
            ( 3, 0, 4, 7 ),   # Front 

            # Upper points
            ( 4, 8, 5 ),      # Left 
            ( 5, 8, 6 ),      # Back 
            ( 6, 8, 7 ),      # Right 
            ( 7, 8, 4 )       # Front
    ]

    edges = [
        # we will define Edges later
    ]

    # Create mesh
    mesh_data = bpy.data.meshes.new("Raised Pyramid")
    mesh_data.from_pydata(vertices, edges, faces)

    # Object using the mesh data
    object = bpy.data.objects.new("Raised Pyramid", mesh_data)

    # Link the Object in the Scene
    bpy.context.collection.objects.link(object)

    # Set location next to previous shape on the Y axis
    object.location = (0, 4, 0)

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Setup variables
    x = 1
    y = 1
    rows = 3
    columns = 9

    # Select shapes
    for obj in bpy.context.scene.objects:
                if obj.type == 'MESH':
                    obj.select_set(True)

    # Duplicate shapes into a row
    while y < rows:
        bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(0, 6, 0)})
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
    for object in shapes:
        object.scale = [0,0,0]
        object.keyframe_insert(data_path = "scale", frame = 1 + offset)
        object.scale = [1,1,5]
        object.keyframe_insert(data_path = "scale", frame = 50 + offset)
        object.scale = [1,1,.5]
        object.keyframe_insert(data_path = "scale", frame = 70 + offset)
        object.scale = [1,1,1]
        object.keyframe_insert(data_path = "scale", frame = 80 + offset)

        offset += 1
    

    # Add object for camera to track
    bpy.ops.object.empty_add()
    empty = bpy.context.active_object

    empty.location = (-15,60,0)
    empty.keyframe_insert(data_path = "location", frame = 1)

    empty.location = (-35,40,0) 
    empty.keyframe_insert(data_path = "location", frame = 140)

    # Add camera
    camera_data = bpy.data.cameras.new(name = 'Animation Camera')
    camera_object = bpy.data.objects.new('Animation Camera', camera_data)
    bpy.context.scene.collection.objects.link(camera_object)

    camera_object.location.x = 18.0
    camera_object.location.y = -23.0
    camera_object.location.z = 7

    camera_object.rotation_euler = (radians(64),radians(0),radians(47))

    camera_object.constraints.new(type='TRACK_TO')
    camera_object.constraints["Track To"].target = empty

    # As the camera is created in script the Blender file
    # requires an active camera for the scene to render animation
    # below sets the active camera
    # camera_object = bpy.context.scene.camera
    bpy.context.scene.camera = camera_object


    # Save the blender file
    # Uncomment if you wish to automatically save
    # bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)

    console("ENDS:")

except Exception as e:
    console(e)