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
whites = [[0, 15], [0, 11], [0, 7], [0, 3], [2, 13], [2, 9], [2, 5], [2, 1], [4, 15], [4, 11], [4, 7], [4, 3]]
blacks = [[10, 13], [10, 9], [10, 5], [10, 1], [12, 15], [12, 11], [12, 7], [12, 3], [14, 13], [14, 9], [14, 5], [14, 1]]

def main(context, type):
    global x_position
    global color_white
    global whites
    global blacks
    
    if type == 'cell':
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
        
    elif type == 'chess':
        for i in range(1, 17, 2):
            for g in range(1, 9):
                bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(x_position, i, 0), scale=(1, 1, 1))
                x_position += 2
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
            x_position = 0
            color_white = not color_white
    
    elif type == 'chips':
        for i in whites:
            bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(i[0], i[1], 0.15), scale=(0.8, 0.8, 0.13))
            obj = bpy.context.active_object
            mat = bpy.data.materials.new(name = 'ColorMaterial')
            obj.data.materials.append(mat)
            mat.diffuse_color = (1.0, 1.0, 1.0, 1.0)
            bpy.context.view_layer.update()
            bpy.context.scene.eevee.use_ssr = True
        for i in blacks:
            bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(i[0], i[1], 0.15), scale=(0.8, 0.8, 0.13))
            obj = bpy.context.active_object
            mat = bpy.data.materials.new(name = 'ColorMaterial')
            obj.data.materials.append(mat)
            mat.diffuse_color = (0.0, 0.0, 0.0, 1.0)
            bpy.context.view_layer.update()
            bpy.context.scene.eevee.use_ssr = True   
        
    elif type == 'white-chip':
        bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(10, 13, 0), scale=(0.8, 0.8, 0.13))
        obj = bpy.context.active_object
        mat = bpy.data.materials.new(name = 'ColorMaterial')
        obj.data.materials.append(mat)
        mat.diffuse_color = (1.0, 1.0, 1.0, 1.0)
        bpy.context.view_layer.update()
        bpy.context.scene.eevee.use_ssr = True
        
    elif type == 'black-chip':
        bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(0.8, 0.8, 0.13))
        obj = bpy.context.active_object
        mat = bpy.data.materials.new(name = 'ColorMaterial')
        obj.data.materials.append(mat)
        mat.diffuse_color = (0.0, 0.0, 0.0, 1.0)
        bpy.context.view_layer.update()
        bpy.context.scene.eevee.use_ssr = True
        
class SimpleCellOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_cell_operator"
    bl_label = "Создать клеточку"

    def execute(self, context):
        main(context, 'cell')
        return {'FINISHED'}

class SimpleChessOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_chess_operator"
    bl_label = "Создать шахматную доску"

    def execute(self, context):
        main(context, 'chess')
        return {'FINISHED'}

class SimpleWhiteChipOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_white_chip_operator"
    bl_label = "Создать белую фишку"

    def execute(self, context):
        main(context, 'white-chip')
        return {'FINISHED'}

class SimpleBlackChipOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_black_chip_operator"
    bl_label = "Создать черную фишку"
    
    def execute(self, context):
        main(context, 'black-chip')
        return {'FINISHED'}

class SimpleChipsOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_chips_operator"
    bl_label = "Создать фишки"
    
    def execute(self, context):
        main(context, 'chips')
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
        layout.label(text="Создать клеточку:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_cell_operator")
        
        layout.label(text="Создать шахматную доску:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_chess_operator")
        
        layout.label(text="Создать фишки:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_chips_operator")
        
        layout.label(text="Создать белую фишку:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_white_chip_operator")
        
        layout.label(text="Создать черную фишку:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_black_chip_operator")

def register():
    bpy.utils.register_class(LayoutDemoPanel)
    bpy.utils.register_class(SimpleCellOperator)
    bpy.utils.register_class(SimpleChessOperator)
    bpy.utils.register_class(SimpleWhiteChipOperator)
    bpy.utils.register_class(SimpleBlackChipOperator)
    bpy.utils.register_class(SimpleChipsOperator)

def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(SimpleCellOperator)
    bpy.utils.unregister_class(SimpleChessOperator)
    bpy.utils.unregister_class(SimpleWhiteChipOperator)
    bpy.utils.unregister_class(SimpleBlackChipOperator)
    bpy.utils.unregister_class(SimpleChipsOperator)

if __name__ == "__main__":
    register()
