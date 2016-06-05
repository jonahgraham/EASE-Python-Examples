loadModule("/System/UI")
loadModule("/System/Platform")

# import logging
# logger = logging.getLogger("py4j")
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

ArrayContentProvider = org.eclipse.jface.viewers.ArrayContentProvider
LabelProvider = org.eclipse.jface.viewers.LabelProvider
ListViewer = org.eclipse.jface.viewers.ListViewer
SWT = org.eclipse.swt.SWT
FillLayout = org.eclipse.swt.layout.FillLayout
RowLayout = org.eclipse.swt.layout.RowLayout
Display = org.eclipse.swt.widgets.Display
Shell = org.eclipse.swt.widgets.Shell
Button = org.eclipse.swt.widgets.Button

def uimain():
    display = Display.getCurrent()
    dialog = Shell(display, SWT.DIALOG_TRIM | SWT.MAX | SWT.RESIZE)
    dialog.setLayout(RowLayout())

    listViewer = ListViewer(dialog)
    listViewer.setLabelProvider(LabelProvider())
    listViewer.setContentProvider(ArrayContentProvider.getInstance())

    # create initial entries
    initialCount = 10
    elements = java.util.ArrayList(["Item {}".format(i) for i in range(initialCount)])
    listViewer.setInput(elements)

    add = Button(dialog, SWT.PUSH)
    add.setText("Add Data")
    class AddDataSelectionListener(object):
        def __init__(self, start):
            self.count = start

        def widgetSelected(self, e):
            elements.append("Item {}".format(self.count))
            self.count += 1
            listViewer.refresh()

        def equals(self, other):
            return self is other
        def hashCode(self):
            return id(self)
        def widgetDefaultSelected(self, e):
            pass
        class Java:
            implements = ['org.eclipse.swt.events.SelectionListener']
    add.addSelectionListener(AddDataSelectionListener(initialCount))

    remove = Button(dialog, SWT.PUSH)
    remove.setText("Remove Selected Data")
    class RemoveDataSelectionListener(object):
        def widgetSelected(self, e):
            for remove in listViewer.getSelection().toArray():
                elements.remove(remove)
            listViewer.refresh()

        def equals(self, other):
            return self is other
        def hashCode(self):
            return id(self)
        def widgetDefaultSelected(self, e):
            pass
        class Java:
            implements = ['org.eclipse.swt.events.SelectionListener']
    remove.addSelectionListener(RemoveDataSelectionListener())

    dialog.pack()
    dialog.open()
    while dialog is not None and not dialog.isDisposed():
        if not display.readAndDispatch():
            display.sleep()
    if not display.isDisposed():
        display.update()


executeUI("uimain()")
