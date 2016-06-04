''' 
Deletes the five java projects created by create5javaprojects.py
'''
loadModule("/System/Resources")
    
for name in ["zag", "zeg", "zig", "zog", "zug"]:
    project = getProject(name)
    project.delete(0, None)