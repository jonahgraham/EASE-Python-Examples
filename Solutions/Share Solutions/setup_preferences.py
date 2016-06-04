# This script was inspired by http://www.vogella.com/tutorials/Eclipse/article.html#improvedeclipsesettings

loadModule('/System/Platform');

def change_preference(location, name, value):
    was = readPreferences(location, name)
    if was != value:
        writePreferences(location, name, value)
        print("Changed: {}/{} from {} to {}".format(location, name, was, value))
    else:
        print("No change needed: {}/{} is already {}".format(location, name, was))

# Automatic placement of semicolon
change_preference("org.eclipse.jdt.ui", "smart_semicolon", "true")
# Auto-escape text pasted into Strings
change_preference("org.eclipse.jdt.ui", "escapeStrings", "true")
# Bracket highlighting
change_preference("org.eclipse.jdt.ui", "enclosingBrackets", "true")
change_preference("org.eclipse.jdt.ui", "highlightBracketAtCaretLocation", "true")
# Type Filters
change_preference("org.eclipse.jdt.ui", "org.eclipse.jdt.ui.typefilter.enabled", "java.awt*;")


print("Done setting all improved settings")
