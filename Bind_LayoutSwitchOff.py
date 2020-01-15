import win32com.client
from tkinter import filedialog

filelist = filedialog.askopenfilenames()
app = win32com.client.Dispatch("AutoCAD.Application")

opened = [i.FullName for i in app.Documents]
print(opened)
for j in filelist:
    print(j)
    if j in opened:
        doc=app.Documents.Item(j)
    else:
        doc = app.Documents.Open(j, False)
    try:
        for i in doc.Blocks:
            if i.IsXref:
                i.bind(True)
        for i in doc.Layers:
            if i.Name == 'G-ANNO-NPLT':
                i.LayerOn = False
            else:
                continue
    finally:
        doc.Close(True)
