bl_info = {
    "name": "Grow Tree",
    "author": "forw4rd",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Properties > Scene > Grow Tree > Создать",
    "description": "Вырастить дерево",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}


import bpy

def main(context):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=1.5, enter_editmode=False, align='WORLD', location=(0, 0, 4), scale=(1, 1, 1))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.3, depth=3, enter_editmode=False, align='WORLD', location=(0, 0, 1.5), scale=(1, 1, 1))
    bpy.context.scene.eevee.use_ssr = True
    bpy.context.scene.eevee.use_ssr = True


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Вырастить дерево"


    def execute(self, context):
        main(context)
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

        # Create a simple row.
        layout.label(text=" Simple Row:")

        row = layout.row()
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")

        # Create an row where the buttons are aligned to each other.
        layout.label(text=" Aligned Row:")

        row = layout.row(align=True)
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")

        # Create two columns, by using a split layout.
        split = layout.split()

        # First column
        col = split.column()
        col.label(text="Column One:")
        col.prop(scene, "frame_end")
        col.prop(scene, "frame_start")

        # Second column, aligned
        col = split.column(align=True)
        col.label(text="Column Two:")
        col.prop(scene, "frame_start")
        col.prop(scene, "frame_end")

        # Big render button
        layout.label(text="Создать:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_operator")

def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(LayoutDemoPanel)


if __name__ == "__main__":
    register()
