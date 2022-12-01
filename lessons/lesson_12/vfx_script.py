import bpy
import random

# Add Scene Objects 
# Add Material
# Add Shaders
# Animate Scene
# Render Video

z = 2 * random.random()
y = 3 * random.random()

bpy.ops.mesh.primitive_cube_add(location=(0, y, z))
bpy.ops.object.constraint_add(type='FOLLOW_PATH')
bpy.context.object.constraints["Follow Path"].target = bpy.data.objects["MotionCubePath"]

r = 2 * random.random()

z = z * 2 * random.random()
y = y * 3 * random.random()

bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=(0, y, z))
bpy.ops.object.constraint_add(type='FOLLOW_PATH')
bpy.context.object.constraints["Follow Path"].target = bpy.data.objects["MotionCubePath"]

