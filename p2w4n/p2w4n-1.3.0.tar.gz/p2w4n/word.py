# 在文档末尾 粘贴
def append(doc):
    docRange = doc.Range()
    docRange.Collapse(0) # wdCollapseEnd	0; wdCollapseStart	1
    try: 
        docRange.Paste() 
    except Exception as e:
        print(f'append PPT notes to Word failed: {e}')
        return
def appendText(doc, text):
    docRange = doc.Range()
    docRange.InsertAfter(text)
def appendJPGFile(doc, jpg):
    appendText(doc, "\r\n\t")
    docRange = doc.Range()
    docRange.Collapse(0)
    docRange.InlineShapes.AddPicture(jpg)
    appendText(doc, "\r\n")