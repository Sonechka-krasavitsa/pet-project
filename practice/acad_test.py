import win32com.client
from pythoncom import VT_R8, VT_ARRAY

app = win32com.client.Dispatch("AutoCAD.Application")
# doc = app.Documents.Add()
pointA = win32com.client.VARIANT(VT_ARRAY | VT_R8, [0, 0, 0]) #конвертирует координаты в читабельный для винды вид
# pointB = win32com.client.VARIANT(VT_ARRAY | VT_R8, [10, 5, 20])
# doc.ModelSpace.AddLine(pointA, pointB)

doc_address = "C:\\Users\\Sonya\\Desktop\\python\\temp\\main file.dwg"
xref_address = "C:\\Users\\Sonya\\Desktop\\python\\temp\\xref.dwg"
# Открываем определенный файл, делаем Xref и биндим
doc = app.Documents.Open(doc_address)
xref = doc.ModelSpace.AttachExternalReference(xref_address,"myxref",pointA,1.0,1.0,1.0,0.0,True)
doc.Blocks.Item(xref.name).Bind(True)