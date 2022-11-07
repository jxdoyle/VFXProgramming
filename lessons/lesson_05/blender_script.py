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

for result in bpy.data.collections:
    if result.name == collection.name:
        for object in result.objects:
            object.location = (random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)) # Translate
            console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
            object.rotation_euler = (random.random(), random.random(), random.random()) # Rotation
            console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
            object.rotation_euler = (radian_rotation, radian_rotation, radian_rotation) # Rotation
            console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
            object.rotation_euler = (radians(30), radians(30), radians(30)) # Rotation
            console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
            object.scale = (random.random(), random.random(), random.random()) # Scale
            console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")

            # Create a Modifier
            mod_01 = object.modifiers.new("Scripted Modifier SUBSURF",'SUBSURF')
            mod_01.levels = 6
            #mod_02 = object.modifiers.new("Scripted Modifier","SOLIDIFY")
            #mod_03 = object.modifiers.new("Scripted Modifier","WIREFRAME")

            for face in object.data.polygons:
                face.use_smooth = True

            # Create a Displacement Modifier
            mod_02 = object.modifiers.new("Scripted Modifier DISPLACEMENT", 'DISPLACE')

            # Create Texture for Displacement
            tex_01 = bpy.data.textures.new("Scripted Texture DISTORTED_NOISE", 'DISTORTED_NOISE')

            # Assign the texture to the displacement modifier
            mod_02.texture = tex_01

            # Create a Material
            material_01 = bpy.data.materials.new(name="Scripted Material")

            # Assign the material to Object
            object.data.materials.append(material_01)

            # Material will use nodes
            material_01.use_nodes = True

            # Assign Node Tree to a Node
            node_01 = material_01.node_tree.nodes

            # Setup a material output
            material_output_01 = node_01.get("Material Output")

            # Setup Shader
            node_shader = node_01.new("ShaderNodeEmission")
            node_shader.inputs[0].default_value = (1.0, 0.0, 0.0, 1.0) # Set Shader Color 
            
            # Link Shader
            shader_links = material_01.node_tree.links
            
            linked_shader = shader_links.new(node_shader.outputs[0], material_output_01.inputs[0])







console("ENDS:")