bl_info = {
    "name": "Cube Addon",
    "author": "James",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > N",
    "description": "Adds and removes cubes",
    "warning": "",
    "doc_url": "",
    "category": "",
}


import bpy
from random import randint
from bpy.types import (Panel, Operator)
import os
os.system('cls' if os.name == 'nt' else 'clear')


class AddCubes(bpy.types.Operator):
    bl_idname = "add.cubes"
    bl_label = "Add Cubes"
        
    def execute(self, context):
        
        location_values = []
        selection_list = []
        name_keys = []
        cube_dict = {}
        count = 20

        class Coords():
            def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z

            # add location values to list
            def createValues():
                for i in range(count):
                    location_values.append(Coords(  x = randint(-20,20), 
                                                    y = randint(-20,20), 
                                                    z = randint(-20,20)))

        # call function
        Coords.createValues()
        
        # run through list adding cubes
        for i in range(len(location_values)):
            bpy.ops.mesh.primitive_cube_add(location=(location_values[i].x, location_values[i].y, location_values[i].z))

            # grab the name of the cubes as they're being made and add them to a list
            selection_list.append(bpy.context.selected_objects)
            for obj in bpy.context.selected_objects:
                name_keys.append(obj.name)  
                
        # create dictionary from the cube names and the location values
        cube_dict = {name_keys[i]: location_values[i] for i in range(len(name_keys))} 
        
        return {'FINISHED'}
    
    
class RemoveCubes(bpy.types.Operator):
    bl_idname = "remove.cubes"
    bl_label = "Remove Cubes"

    def execute(self, context):
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH':
                obj.select_set(True)
            
        bpy.ops.object.delete()
        
        return {'FINISHED'}


class CustomPanel(bpy.types.Panel):
    bl_label = "Cube Panel"
    bl_idname = "OBJECT_PT_cubes"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Cube Panel"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator(AddCubes.bl_idname, text="Add", icon='MATCUBE')
        row.operator(RemoveCubes.bl_idname, text="Remove", icon='CANCEL')


from bpy.utils import register_class, unregister_class

_classes = [
    AddCubes,
    RemoveCubes,
    CustomPanel
]

def register():
    for cls in _classes:
        register_class(cls)

def unregister():
    for cls in _classes:
        unregister_class(cls)

if __name__ == "__main__":
    register()