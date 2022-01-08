import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "TestPanel"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'New Addon'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Sample Text", icon ='ORIENTATION_GIMBAL')
        row = layout.row()
        row.operator("mesh.primitive_cube_add")
        row.operator("mesh.primitive_uv_sphere_add")
        
        
def register():
    bpy.utils.register_class(TestPanel)
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    

if __name__ == "__main__":
    register()