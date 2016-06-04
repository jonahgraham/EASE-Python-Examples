# name			: Explore from here (Solution)
# popup			: enableFor(org.eclipse.core.resources.IResource)
# description	: Start a file browser using current selection

import subprocess

loadModule('/System/UI')

is_instance_of = py4j.java_gateway.is_instance_of

selection = getSelection()
if is_instance_of(gateway, selection, org.eclipse.jface.viewers.IStructuredSelection):
	selection = selection.getFirstElement()
	
if not is_instance_of(gateway, selection, org.eclipse.core.resources.IResource):
	selection = adapt(selection, org.eclipse.core.resources.IResource)

if is_instance_of(gateway, selection, org.eclipse.core.resources.IFile):
	selection = selection.getParent()
	
if is_instance_of(gateway, selection, org.eclipse.core.resources.IContainer):
	subprocess.call(["explorer.exe", selection.getLocation().toFile().toString()])
	
