loadModule('/System/Resources')
loadModule('/System/UI')

# Access the markers class directly
IMarker = org.eclipse.core.resources.IMarker

for ifile in findFiles("*.java"):
    file_name = str(ifile.getLocation())
    with open(file_name) as f:
        for line_no, line in enumerate(f, start=1):
            if "printStackTrace" in line:
                marker = ifile.createMarker(IMarker.TASK)
                marker.setAttribute(IMarker.TRANSIENT, True)
                marker.setAttribute(IMarker.LINE_NUMBER, line_no)
                marker.setAttribute(IMarker.MESSAGE, "Fix in Sprint 2: " + line.strip())
# XXX: createProblemMarker was added to Resources module after this example was written,
# consider changing to the new method.
#                 createProblemMarker(None, ifile, line_no,
#                                     "Fix in Sprint 2: " + line.strip(),
#                                     IMarker.TASK, True)

showView("Tasks")
