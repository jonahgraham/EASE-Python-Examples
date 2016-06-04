loadModule('/System/UI')

def find_replace(find, replace):
    editor = getActiveEditor()
    doc = editor.getDocumentProvider().getDocument(editor.getEditorInput())
    selection = editor.getSelectionProvider().getSelection()
    text = selection.getText()
    after = text.replace(find, replace)
    if text != after:
        doc.replace(selection.getOffset(), selection.getLength(), after)

executeUI("find_replace('private', 'public')")
