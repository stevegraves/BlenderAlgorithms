import bpy

num = 20
offset = 2

while num > 0:
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(offset, 0, 0), scale=(1, offset, offset))
    num -= 1
    offset += 2
