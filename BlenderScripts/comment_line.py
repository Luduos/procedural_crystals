import bpy

class CommentLineOperator(bpy.types.Operator):
    bl_idname = 'text.comment_line'
    bl_label = 'Comment a line'

    def execute(self, context):
        bpy.ops.text.select_line()
        bpy.ops.text.comment()
        return {'FINISHED'}

bpy.utils.register_class(CommentLineOperator)
bpy.utils.unregister_class(CommentLineOperator)