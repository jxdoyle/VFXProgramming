import bpy

def console(info):

    for windows in bpy.context.window_manager.windows:
        screens = windows.screen
        for areas in screens.areas:
            if areas.type == 'CONSOLE':
                bpy.ops.console.scrollback_append({'window': windows, 'screen': screens, 'area': areas}, text=str(info), type='OUTPUT')
