loadModule("/System/Platform")
loadModule("/System/UI")

ArrayContentProvider = org.eclipse.jface.viewers.ArrayContentProvider
LabelProvider = org.eclipse.jface.viewers.LabelProvider
ListViewer = org.eclipse.jface.viewers.ListViewer
SWT = org.eclipse.swt.SWT
FillLayout = org.eclipse.swt.layout.FillLayout;
Display = org.eclipse.swt.widgets.Display;
Shell = org.eclipse.swt.widgets.Shell;

class MyListViewer(object):
    def __init__(self, shell):
        v = ListViewer(shell, SWT.H_SCROLL | SWT.V_SCROLL)
        v.setLabelProvider(LabelProvider())
        v.setContentProvider(ArrayContentProvider.getInstance())
        v.setInput(self.createModel())
        
    def createModel(self):
        elements = ["Item %s" % i for i in range(10)]
        return elements

        
def uimain():
    display = Display.getCurrent()
    shell = Shell(display)
    shell.setLayout(FillLayout())
    MyListViewer(shell)
    shell.open()

executeUI("uimain()")
# while True:
#     print("Still running")
#     time.sleep(1)
