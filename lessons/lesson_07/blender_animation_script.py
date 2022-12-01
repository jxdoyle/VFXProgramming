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

console("Defining a Cube Mesh")

# Shape Vertices
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

# Shape Vertices
vertices = [
        ( -1.0,   -1.0,   -1.0 ), # [0] Vertex 1
        ( -1.0,   +1.0,   -1.0 ), # [1] Vertex 2
        ( +1.0,   +1.0,   -1.0 ), # [2] Vertex 3
        ( +1.0,   -1.0,   -1.0 ), # [3] Vertex 4
        ( -1.0,   -1.0,   +1.0 ), # [4] Vertex 5
        ( -1.0,   +1.0,   +1.0 ), # [5] Vertex 6
        ( +1.0,   +1.0,   +1.0 ), # [6] Vertex 7
        ( +1.0,   -1.0,   +1.0 )  # [7] Vertex 8
]

# Define faces (index of vertices above)
faces = [
        (0, 1, 2, 3), # Front Face
        (7, 6, 5, 4), # Back Face
        (4, 5, 1, 0), # Left Face
        (7, 4, 0, 3), # Bottom Face
        (6, 7, 3, 2), # Right Face
        (5, 6, 2, 1)  # Top Face
]

edges = [
    # we will define Edges later
]

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
        # Create mesh
        mesh_data = bpy.data.meshes.new("mesh_from_data")
        mesh_data.from_pydata(vertices, edges, faces)
        
        # Object using the mesh data
        object = bpy.data.objects.new("mesh_object", mesh_data)
        # Link the Object in the Scene
        bpy.context.collection.objects.link(object)

        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        object.location =(x, y, z)


    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    # Setup frame increment
    frames = 1
    frame_increment = 5
    offset = 10 # makes each object look a bit more dynamic
    frame_count = 80 # Max number of frames in scene

    # Set the frame count for the number of frames
    bpy.context.scene.frame_end = frame_count

    # Tracking
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    last_object = None

    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:

                # Starting Location
                frames = frame_increment
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")

                # Transform Location
                frames += frame_increment
                object.location = (random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)) # Translate
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

                if object.location.x < min_x:
                    min_x = object.location.x

                if object.location.x > max_x:
                    max_x = object.location.x

                if object.location.y < min_y:
                    min_y = object.location.y

                if object.location.y > max_y:
                    max_y = object.location.y


                offset += 1

                last_object = object
    
    # Add Object for camera to track
    bpy.ops.object.empty_add()
    empty = bpy.context.active_object

    look_at_y = ((max_y - min_y) / 2 ) + min_y
    #empty.location = (min_x, min_y, 0) # Translate
    empty.location = last_object.location
    console(f"Translation => x:{empty.location.x}, y:{empty.location.y}, x:{empty.location.z}")
    empty.keyframe_insert(data_path="location", frame=frames)

    empty.location = (max_x + 5, max_y + 5, last_object.location.z) # Translate
    console(f"Translation => x:{empty.location.x}, y:{empty.location.y}, x:{empty.location.z}")
    empty.keyframe_insert(data_path="location", frame=frame_count)

    # Add Camera
    camera_data = bpy.data.cameras.new(name='Animation Camera')
    camera_object = bpy.data.objects.new('Animation Camera', camera_data)
    bpy.context.scene.collection.objects.link(camera_object)

    camera_object.location.x = 7.0
    camera_object.location.y = -7.0
    camera_object.location.z = 5

    camera_object.rotation_euler = (radians(64),radians(0),radians(47))

    camera_object.constraints.new(type='TRACK_TO')
    camera_object.constraints["Track To"].target = empty

    # As the camera is created in script the Blender file
    # requires an active camera for the scene to render animation
    # below sets the active camera
    bpy.context.scene.camera = camera_object

    # Add a light
    light_data = bpy.data.lights.new(name="Point Light", type='POINT')
    light_object = bpy.data.objects.new(name="Point Light", object_data=light_data)
    light_data.energy = 100 # 100 Watts
    bpy.context.scene.collection.objects.link(light_object)
    light_object.location = camera_object.location

    # Save the blender file
    bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)

    console("ENDS:")

except Exception as e:
    console(e)