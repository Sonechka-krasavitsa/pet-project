import win32com.client
from pythoncom import VT_R8, VT_ARRAY, VT_I2, VT_VARIANT, com_error
from tkinter import filedialog

# filelist = filedialog.askopenfilenames()
# print(filelist)

# app = win32com.client.Dispatch("AutoCAD.Application")
# doc = app.Documents.Open(filelist[0])
app = win32com.client.Dispatch("AutoCAD.Application")
doc = app.ActiveDocument
# print(doc.Name)
doc.SetVariable('FILEDIA', 0)
doc.SendCommand("-PUBLISH \n")
doc.SendCommand("D:/1.dsd \n")
doc.SetVariable('FILEDIA', 1)