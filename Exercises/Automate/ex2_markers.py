# 1. use the resources module 
 
IMarker = org.eclipse.core.resources.IMarker
 
# 2. TODO:use findFiles method to get all *.java files in the workspace
# 3. use 'for' loop to iterate over files, (using ifile as your variable name)

# 4. Uncomment these lines to get file location, open file and iterate through lines
# 
#    file_name = str(ifile.getLocation())
#    with open(file_name) as f:
#        for line_no, line in enumerate(f, start=1):
#            if "TODO" in line:

# 5. Create a marker(Hint method is on ifile and use type IMarker.TASK

# 6. set marker attribute e.g IMarker.LINE_NUMBER and IMarker.MESSAGE
