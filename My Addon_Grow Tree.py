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
x_position = 0
color_white = True 

def main(context, type):
    global x_position
    global color_white
    if type == 'tree':
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=1.5, enter_editmode=False, align='WORLD', location=(0, 0, 4), scale=(1, 1, 1))
        bpy.ops.mesh.primitive_cylinder_add(radius=0.3, depth=3, enter_editmode=False, align='WORLD', location=(0, 0, 1.5), scale=(1, 1, 1))
        bpy.context.scene.eevee.use_ssr = True
    elif type == 'bush':
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=2, enter_editmode=False, align='WORLD', location=(x_position, 0, 2), scale=(2, 2, 2))
        bpy.context.scene.eevee.use_ssr = True
        x_position += 4
    elif type == 'cell':
        bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(x_position, 0, 0), scale=(1, 1, 1))
        obj = bpy.context.active_object
        mat = bpy.data.materials.new(name = 'ColorMaterial')
        obj.data.materials.append(mat)
        if color_white == False:
            mat.diffuse_color = (0.0, 0.0, 0.0, 1.0)
        else:
            mat.diffuse_color = (1.0, 1.0, 1.0, 1.0)
        color_white = not color_white
        bpy.context.view_layer.update()
        bpy.context.scene.eevee.use_ssr = True
        x_position += 2
        
    elif type == 'some-sells':
        for i in range(0, 7, 2):
            bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(x_position, i, 0), scale=(1, 1, 1))
            bpy.context.scene.eevee.use_ssr = True
        x_position += 2
        
class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Вырастить дерево"


    def execute(self, context):
        main(context, 'tree')
        return {'FINISHED'}

class SimpleBushOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_bush_operator"
    bl_label = "Вырастить куст"

    def execute(self, context):
        main(context, 'bush')
        return {'FINISHED'}
    
class SimpleCellOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_cell_operator"
    bl_label = "Создать клеточку"

    def execute(self, context):
        main(context, 'cell')
        return {'FINISHED'}

class SimpleSomeCellOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_some_cell_operator"
    bl_label = "Создать несколько клеточек"

    def execute(self, context):
        main(context, 'some-sells')
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
        layout.label(text="Создать дерево:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_operator")

        layout.label(text="Создать куст:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_bush_operator")

        layout.label(text="Создать клеточку:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_cell_operator")
        
        layout.label(text="Создать несколько клеточек:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_some_cell_operator")

def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(LayoutDemoPanel)
    bpy.utils.register_class(SimpleBushOperator)
    bpy.utils.register_class(SimpleCellOperator)
    bpy.utils.register_class(SimpleSomeCellOperator)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(SimpleBushOperator)
    bpy.utils.register_class(SimpleCellOperator)
    bpy.utils.register_class(SimpleSomeCellOperator)

if __name__ == "__main__":
    register()
