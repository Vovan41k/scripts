bl_info = {
    "name": "Model",
    "author": "forw4rd",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Properties > Scene > Model > Создать",
    "description": "Создать модель",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}


import bpy

def main(context, type):
      
    if type == 'model':
        file_path = 'C:\\Users\\User\\Documents\\dino\\mm_frame.obj'
        bpy.ops.import_scene.obj(filepath=file_path)
        obj = bpy.context.selected_objects[0]
        obj.location = (1, 1, z_location)
class SimpleModelOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_model_operator"
    bl_label = "Создать 3d модель"
    
    def execute(self, context):
        main(context, 'model')
        return {'FINISHED'}

class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Grow Tree"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Big render button
        layout.label(text="Создать модель:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_model_operator")

def register():
    bpy.utils.register_class(LayoutDemoPanel)
    bpy.utils.register_class(SimpleModelOperator)

def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(SimpleModelOperator)
    
if __name__ == "__main__":
    register()
