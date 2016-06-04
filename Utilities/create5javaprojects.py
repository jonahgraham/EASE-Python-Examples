''' 
Creates five projects with java nature
'''
loadModule("/System/Resources")

def array(l, element_type=None):
    ''' 
    Convert list l to a Java array of element_type.
    If element_type is None, java.lang.Object is used. 
    '''
    ## TODO type inference
    if element_type is None:
        element_type = java.lang.Object
    array_len = len(l)
    new_array = gateway.new_array(element_type,1)
    for i, entry in enumerate(l):
        new_array[i] = entry
    return new_array

for name in ["zag", "zeg", "zig", "zog", "zug"]:
    project = createProject(name)
   # description = project.getDescription()
   # natureId = org.eclipse.jdt.core.JavaCore.NATURE_ID
   # description.setNatureIds(array([natureId], element_type=java.lang.String))
   # project.setDescription(description, None)