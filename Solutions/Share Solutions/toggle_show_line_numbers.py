loadModule('/System/Platform')
loadModule('/System/UI')

def toggle_in_ui():
    was = readPreferences("org.eclipse.ui.editors", "lineNumberRuler", True)
    writePreferences("org.eclipse.ui.editors", "lineNumberRuler", not was)


executeUI("toggle_in_ui()")
