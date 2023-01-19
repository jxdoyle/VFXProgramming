import bpy

def console(info):
    """
    Get the window context
    Get the Screen
    Get the Area Type
    Append to Console
    """
    for windows in bpy.context.window_manager.windows:
        screens = windows.screen
        for areas in screens.areas:
            if areas.type == 'CONSOLE':
                bpy.ops.console.scrollback_append({'window': windows, 'screen': screens, 'area': areas}, text=str(info), type='OUTPUT')