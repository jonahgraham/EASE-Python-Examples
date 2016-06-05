# 0. Add in magic headers to add this to the pop-up menu
#   ensure it is enabled for selections of type org.eclipse.core.resources.IResource

import subprocess

# 1. load the UI module

is_instance_of = py4j.java_gateway.is_instance_of

# 2. get the current selection (Hint: use method from UI module)
# selection = 

if is_instance_of(gateway, selection, org.eclipse.jface.viewers.IStructuredSelection):
    print(selection) # 3. get the first element if is a structured Selection
    
if not is_instance_of(gateway, selection, org.eclipse.core.resources.IResource):
    print(selection) # 4. adapt the selection to org.eclipse.core.resources.IResource (Hint: use method from UI module)

if is_instance_of(gateway, selection, org.eclipse.core.resources.IFile):
    print(selection)  # 5. if it is a file get its parent
    
if is_instance_of(gateway, selection, org.eclipse.core.resources.IContainer):
    print(selection)  #6. if a container, then obtain the full path to the directory
    # 7. invoke explorer.exe using a subprocess.call() passing in path as argument
    
