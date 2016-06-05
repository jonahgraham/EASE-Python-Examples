# Demonstrate the command line operation by showing the names
# of all the projects in the workspace

# Run it from the command line like so:
#   <path>/eclipse
#      -data <path>/workspace
#      -consoleLog -noSplash
#      -application org.eclipse.ease.runScript
#      -script <path>/show_projects_in_workspace.py
#
# Jonah's machine example:
# /scratch/ease/ecf/eclipse/eclipse -data /scratch/ease/ecf/workspace -noSplash -application org.eclipse.ease.runScript -script /scratch/ease/ecf/git/EASE-Python-Examples/Solutions/Share\ Solutions/show_projects_in_workspace.py

loadModule('/System/Resources')

workspace = getWorkspace()
print("Information about workspace ({})".format(workspace.getLocation()))

for i, project in enumerate(workspace.getProjects()):
    print("Project {}: {} ({})".format(i,
                                       project.getName(),
                                       project.getLocation()))
