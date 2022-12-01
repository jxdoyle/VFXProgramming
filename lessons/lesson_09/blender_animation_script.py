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

def createMaterial(name):
    #check if material already exists
    material = bpy.data.materials.get(name)

    # If there no materials of that name then create one
    if material is None:
        # creater the Material
        material = bpy.data.materials.new(name)
    
    # Not any objects assigned this material name will have
    # their appearance changed

    # Used Shader Nodes (Opening Shader Editor will show nodes)
    material.use_nodes = True

    # Clear any exiting Nodes
    if material.node_tree:
        material.node_tree.links.clear()
        material.node_tree.nodes.clear()

    return material

def EmissionShader(name, red, green, blue):

    material = createMaterial(name)

    nodes = material.node_tree.nodes
    links = material.node_tree.links

    # Output to the Material Output Nore
    output = nodes.new(type='ShaderNodeOutputMaterial')

    shader = nodes.new(type='ShaderNodeEmission')
    nodes["Emission"].inputs[0].default_value = (red, green, blue, 1)
    nodes["Emission"].inputs[1].default_value = 1

    # This links the output of the Emission Shader
    # to the Input of the Material Output Shader
    links.new(shader.outputs[0], output.inputs[0])

    return material

console("STARTS:")

console("Defining a Cube Mesh")

# Shape Vertices
#
#		  (-1.0, +1.0, +1.0)          (+1.0, +1.0, +1.0)
#		          [5]                          [6]
#		          #------------{5}--------------#
#		         /|                            /|
#		       {8}|                          {9}|
#	  (-1.0, +1.0, -1.0)           (+1.0, +1.0, -1.0)
#		  [1] /                         [2] /
#		     #-------------{1}-------------#    |
#		     |   {4}                       |   {6}
#		     |    |                        |    |
#		     |   [4]                       |   [7]
#		  (-1.0, -1.0, +1.0)         (+1.0, -1.0, +1.0)
#		    {0}   #------------{7}--------------#
#		     |   /                        {2}  /
#		     | {11}                        | {10}
#		     | /                           | /
#		     |/                            |/
#		     #--------------{3}------------#
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

# Define Edges (index of vertices above)
edges = [
        (0, 1), # {0} Edge 1
        (1, 2), # {1} Edge 2
        (2, 3), # {2} Edge 3
        (3, 0), # {3} Edge 4
        (4, 5), # {4} Edge 5
        (5, 6), # {5} Edge 6
        (6, 7), # {6} Edge 7
        (7, 4), # {7} Edge 8
        (1, 5), # {8} Edge 9
        (2, 6), # {9} Edge 10
        (3, 7), # {10} Edge 11
        (0, 4), # {11} Edge 12
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
    object.location = (x, y, z)

    # Create a Shader and Modify
    # https://docs.blender.org/manual/en/latest/render/materials/index.html

    material = EmissionShader("Scripted_Shader_Emission", 0.5, 1.0, 0.0)

    # Check if Object has already been assigned a material
    if object.data.materials:
        # Assign to first material slot
        object.data.materials[0] = material
    else:
        # We have more than one material so append
        # Note with more than one material we will need to 
        # combine final colors
        object.data.materials.append(material)


    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                if(object.type == "MESH"):
                    mesh = object.data
                    vertices = mesh.vertices
                    faces = mesh.polygons
                    edges = mesh.edges

                    vertex_count = len(mesh.vertices)
                    polygon_count = len(mesh.polygons)
                    edge_count = len(mesh.edges)
                    
                    print(f"Vertex Count {vertex_count}")
                    vector = "Vector:"
                    for v in vertices:
                        print(v.co)
                        vector += f"Vector {v.index} => " # Vector index
                        vector += f"x:{v.co.x} y:{v.co.y} z:{v.co.z} " # vertex
                    print(vector) # Print to make console
                    console(vector) # Print to blender console

                    print(f"********************************************************************************")

                    print(f"Polygon or Faces Count {polygon_count}")
                    face_list = "Faces:"
                    for f in faces:
                        for index in f.vertices: # Vertices in Faces
                            face_list += f"Face {f.index} => " # Face index
                            face_list += f"[{index}] " # vertex index
                            face_list += f"x:{vertices[index].co.x} y:{vertices[index].co.y} z:{vertices[index].co.z} " # vertex index
                    print(face_list) # Print to make console
                    console(face_list) # Print to blender console

                    print(f"********************************************************************************")

                    print(f"Edge Count {edge_count}")
                    edges_list = "Edges:"
                    for e in edges: # Edges
                        for index in e.vertices: # Vertices in Edges
                            edges_list += f"Edge {e.index} => " # edge index
                            edges_list += f"[{index}] " # vertex index
                            edges_list += f"x:{vertices[index].co.x} y:{vertices[index].co.y} z:{vertices[index].co.z} " # vertex index
                    print(edges_list) # Print to make console
                    console(edges_list) # Print to blender console
                else:
                    print("Not a MESH") 

    console("ENDS:")

except Exception as e:
    print(e)
    console(e)