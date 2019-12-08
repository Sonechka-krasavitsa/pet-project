import win32com.client
from pythoncom import VT_R8, VT_ARRAY

app = win32com.client.Dispatch("AutoCAD.Application")
# doc = app.Documents.Add()
pointA = win32com.client.VARIANT(VT_ARRAY | VT_R8, [0, 0, 0])
pointB = win32com.client.VARIANT(VT_ARRAY | VT_R8,
                                 [-1000, -1000, 0])
# конвертирует координаты в читабельный для винды вид
def crd(coord):
    return win32com.client.VARIANT(VT_ARRAY | VT_R8, coord)

doc_address = "C:\\Users\\Sonya\\Desktop\\python\\RevTag\\test_block.dwg"
# doc = app.Documents.Open(doc_address)
doc = app.ActiveDocument
# doc.Document.SendCommand(PUBLISH)
# new_block = doc.ModelSpace.InsertBlock(pointA, "RevTag", 1.0, 1.0, 1.0, 0.0)
# line=doc.ModelSpace.AddPolyline(pointA, pointB)
# coord=

new_dot = doc.ModelSpace.AddPoint(pointB)
coord = new_dot.Coordinates
print(coord)
block2 = doc.ModelSpace.InsertBlock(crd(coord), "RevTag", 1.0, 1.0, 1.0, 0.0)
# print(block2.basePoint.Coordinates)
print(doc.ModelSpace.Count)
