import win32com.client
from tkinter import filedialog

filelist = filedialog.askopenfilenames()
print(filelist)
target_folder = filedialog.askdirectory()

app = win32com.client.Dispatch("AutoCAD.Application")
for i in filelist:
    doc = app.Documents.Open(i, False)
    all_layout_info = doc.Layouts
    all_layout_name = []
    for j in all_layout_info:
        if j.Name == "Model":
            continue
        else:
            all_layout_name.append(j.Name)
    print(all_layout_name)
    print(doc.Name)
    doc.Close()