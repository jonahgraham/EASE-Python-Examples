loadModule('/System/Resources')

for iproject in getWorkspace().getProjects():
    if not iproject.isOpen():
        continue
    
    ifile = iproject.getFile("README.md")
    
    if not ifile.exists():
        contents = "# " + iproject.getName() + "\n\n" 
        if iproject.hasNature("org.eclipse.jdt.core.javanature"):
            contents += "A Java Project\n"
        elif iproject.hasNature("org.python.pydev.pythonNature"):
            contents += "A Python Project\n"
        writeFile(ifile, contents)