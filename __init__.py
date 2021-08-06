import bpy
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "FrameLocker",
    "author" : "GarageMan",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "Dope Sheet View Tab",
    "warning" : "",
    "category" : "Animation"
}

def CancelAnim(self, context):
    bpy.ops.screen.animation_cancel(restore_frame=True)
    


def BlockUpdate(self, context):
     if(context.scene.ToBlock == True): 
         #this is the case to block
         bpy.app.handlers.frame_change_pre.append(CancelAnim)
     else:
         bpy.app.handlers.frame_change_pre.remove(CancelAnim)
         #this is the case to remove the handler.

class BlockerPanel(bpy.types.Panel):
    bl_label = "Lock Frame"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'DOPESHEET_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Anim Blocker"
    bl_context = "scene"



    Block : bpy.props.BoolProperty(name="ToBlock")

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.prop(context.scene, 'ToBlock')



def register():
    bpy.types.Scene.ToBlock = bpy.props.BoolProperty(
        name='Lock',
        update = BlockUpdate
    )
    bpy.utils.register_class(BlockerPanel)


def unregister():
    del bpy.types.Scene.ToBlock
    bpy.utils.unregister_class(BlockerPanel)

