bl_info = {
    "name": "Workspace Importer",
    "author": "gogo",
    "version": (0, 0, 1),
    "blender": (2, 82, 0),
    "description": "Import workspaces from startup.blend",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "category": "User Interface"
}


import bpy
from bpy.props import (
    PointerProperty,
    BoolProperty,
    EnumProperty,
)
import os


def get_workspace_list_callback(scene, context):
    items = []

    filepath = os.path.join(bpy.utils.resource_path('USER'), "config\\startup.blend")
    # link startup.blend file
    with bpy.data.libraries.load(filepath, link=True) as (data_from, data_to):
        data_to.workspaces = data_from.workspaces

    for wk in data_to.workspaces:
        items.append((wk, wk, ""))

    return items


class MYWORKSPACE_OT_import(bpy.types.Operator):
    bl_idname = "myworkspace.import"
    bl_label = "Import Workspace "
    bl_description = "Import the workspace from startup.blend"
    # This Operattion(=append) can't undo.
    # bl_options = {'REGISTER', 'UNDO'}

    '''
    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'
    '''
    
    def execute(self, context):
        
        propGrp = context.scene.mywrkspc
        
        if context.object is not None:
            # Edit-mode somotimes gets an error when importing.
            bpy.ops.object.mode_set(mode='OBJECT')

        blendfile = os.path.join(bpy.utils.resource_path('USER'), "config\\startup.blend")
        section = "\\WorkSpace\\"
        wk = propGrp.sWorkspaceList

        filepath = blendfile + section + wk
        directory = blendfile + section
        filename = wk

        before_list = [ws.name for ws in bpy.data.workspaces]
        bpy.ops.wm.append(
            filepath=filepath,
            filename=filename,
            directory=directory
        )
        after_list = [ws.name for ws in bpy.data.workspaces]

        if propGrp.bMakeActive:
            result = list(set(after_list) - set(before_list))
            context.window.workspace = bpy.data.workspaces[result[0]]
        
        return {'FINISHED'}


class MYWORKSPACE_OT_delete(bpy.types.Operator):
    bl_idname = "myworkspace.delete"
    bl_label = "Delete Workspaces "
    bl_description = "Delete other non-active workspaces"
    # This Operattion(=batch_remove) can't undo.
    # bl_options = {'REGISTER', 'UNDO'}

    '''
    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'
    '''
    
    def execute(self, context):
        if context.object is not None:
            bpy.ops.object.mode_set(mode='OBJECT')
        workspaces = [ws for ws in bpy.data.workspaces if ws != context.workspace]
        bpy.data.batch_remove(ids=workspaces)
        
        return {'FINISHED'}


class MYWORKSPACE_PT_import(bpy.types.Panel):
    bl_idname = "MYWORKSPACE_PT_import"
    bl_label = "Workspace Importer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout
        propGrp = context.scene.mywrkspc
        layout.prop(propGrp, property="sWorkspaceList", text="Workspace")
        layout.prop(propGrp, property="bMakeActive", text="Set Active")
        
        layout.operator(MYWORKSPACE_OT_import.bl_idname, text="Import ")
        layout.operator(MYWORKSPACE_OT_delete.bl_idname, text="Delete Other Workspaces")


class MYWORKSPACE_Props(bpy.types.PropertyGroup):
    sWorkspaceList: EnumProperty(
        name="Workspace List",
        description="Workspace to import",
        items=get_workspace_list_callback,
    )
    bMakeActive: BoolProperty(
        name="Make Active",
        description="Make the appended workspace active",
        default=True,
    )


classes = (
    MYWORKSPACE_Props,
    MYWORKSPACE_OT_import,
    MYWORKSPACE_OT_delete,
    MYWORKSPACE_PT_import,
)


def register():
    for i in classes:
        bpy.utils.register_class(i)
    bpy.types.Scene.mywrkspc = PointerProperty(type=MYWORKSPACE_Props)


def unregister():
    del bpy.types.Scene.mywrkspc
    for i in classes:
        bpy.utils.unregister_class(i)
