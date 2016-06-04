'''
Creates five projects with java nature
'''
loadModule("/System/Resources")
include('workspace://Utilities/java_array.py')

# https://dzone.com/articles/use-eclipse-jdt-dynamically

IFolder = org.eclipse.core.resources.IFolder
IProject = org.eclipse.core.resources.IProject
IProjectDescription = org.eclipse.core.resources.IProjectDescription
IWorkspaceRoot = org.eclipse.core.resources.IWorkspaceRoot
ResourcesPlugin = org.eclipse.core.resources.ResourcesPlugin
CoreException = org.eclipse.core.runtime.CoreException
IClasspathEntry = org.eclipse.jdt.core.IClasspathEntry
ICompilationUnit = org.eclipse.jdt.core.ICompilationUnit
IJavaProject = org.eclipse.jdt.core.IJavaProject
IPackageFragment = org.eclipse.jdt.core.IPackageFragment
IPackageFragmentRoot = org.eclipse.jdt.core.IPackageFragmentRoot
IType = org.eclipse.jdt.core.IType
JavaCore = org.eclipse.jdt.core.JavaCore
JavaModelException = org.eclipse.jdt.core.JavaModelException
JavaRuntime = org.eclipse.jdt.launching.JavaRuntime


def create_java_project(name):
    project = getProject(name)
    if project.exists():
        raise Exception("Project {} already exists".format(name))
    project = createProject(name)
    description = project.getDescription()
    natureId = org.eclipse.jdt.core.JavaCore.NATURE_ID
    description.setNatureIds(java_array([natureId], java_type=java.lang.String))
    project.setDescription(description, None)

    javaProject = JavaCore.create(project)

    # set the build path
    buildPath = java_array([JavaCore.newSourceEntry(project.getFullPath().append("src")),
                 JavaRuntime.getDefaultJREContainerEntry()], java_type=IClasspathEntry)

    javaProject.setRawClasspath(buildPath, project.getFullPath().append("bin"), None)

    # create folder by using resources package
    folder = project.getFolder("src")
    folder.create(True, True, None)

    return javaProject

def create_java_package(javaProject, packageName):
    srcFolder = javaProject.getPackageFragmentRoot(javaProject.getProject().getFolder("src"))
    javaPackage = srcFolder.createPackageFragment(packageName, True, None)
    return javaPackage

def create_java_class(javaPackage, className):
    # init code string and create compilation unit
    str = '''package {packageName};

public class {className} {{

    public static void doesNothingUseful() throws Exception {{
        throw new Exception("Exception while doing nothing useful");
    }}

    public static void main(String[] args) {{
        System.out.println("Starting {className}");
        try {{
            doesNothingUseful();
        }} catch (Exception e) {{
            e.printStackTrace();
        }}
    }}

}}
'''.format(packageName=javaPackage.getElementName(), className=className)

    cu = javaPackage.createCompilationUnit("{className}.java".format(className=className), str,
                    False, None);


for name in ["zag", "zeg", "zig", "zog", "zug"]:
    javaProject = create_java_project(name)
    packageName = "com.kichwacoders.{}".format(name)
    javaPackage = create_java_package(javaProject, packageName)
    className = name[0].upper() + name[1:] + "Demo"
    create_java_class(javaPackage, className)

