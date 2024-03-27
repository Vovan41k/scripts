bl_info = {
    "name": "Import Object at Location",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy

from bpy.props import StringProperty, FloatVectorProperty

class ImportObjectAtLocation(bpy.types.Operator):
    bl_idname = "object.import_object_at_location"
    bl_label = "Import Object at Location"
    
    file_path: StringProperty(subtype='FILE_PATH')
    location: FloatVectorProperty(name="Location", default=(0.0, 0.0, 0.0))

    def execute(self, context):
        bpy.ops.import_scene.obj(filepath=self.file_path)
        obj = bpy.context.selected_objects[0]
        obj.location = self.location
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

def menu_func(self, context):
    self.layout.operator(ImportObjectAtLocation.bl_idname)

def register():
    bpy.utils.register_class(ImportObjectAtLocation)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)

def unregister():
    bpy.utils.unregister_class(ImportObjectAtLocation)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)

if __name__ == "__main__":
    register()
