'''Корректировка щитов с дополнительными контактами:
1. Изменение доп контакта, убираем механическую связь
2. Корректируем примечание
'''
import win32com.client
from tkinter import filedialog
from pythoncom import VT_R8, VT_ARRAY, VT_I2, VT_VARIANT

tmp_file_list = filedialog.askopenfilenames()

app = win32com.client.Dispatch("AutoCAD.Application")

for file in tmp_file_list:
    try:
        doc = app.Documents.Open(file, False)

        '''Корректируем доп контакты'''
        for elem in doc.Blocks.item('1_CB_N_AC_LIGHT1'):
            if elem.ObjectName=='AcDbLine' and elem.LinetypeScale==10 and elem.Linetype=='DASHED2':
                elem.Delete()
        for elem in doc.Blocks.item('1_CB_AC_N_SPR'):
            if elem.ObjectName=='AcDbLine' and elem.LinetypeScale==10 and elem.Linetype=='DASHED2':
                elem.Delete()
            else:
                continue

        '''Замена доп контакта открытый на закрытый'''
        point = win32com.client.VARIANT(VT_ARRAY | VT_R8, (1000, 1000, 0.0))
        block_name = "C:\\Users\\SoAlekseeva\\Desktop\\source.dwg"
        tmp = doc.ModelSpace.InsertBlock(point, block_name, 1.0, 1.0, 1.0, 0.0)
        tmp.Delete()
        for elem in doc.Blocks.item('1_CB_N_AC_LIGHT1'):
            if elem.ObjectName == 'AcDbBlockReference' and elem.EffectiveName == 'CNO':
                coord = elem.InsertionPoint
                elem.Delete()
            else:
                continue
        doc.Blocks.Item('1_CB_N_AC_LIGHT1').InsertBlock(win32com.client.VARIANT(VT_ARRAY | VT_R8, coord), 'CNC', 1.0,
                                                        1.0, 1.0, 0.0)
        doc.SendCommand('ATTSYNC\n' + 'Name\n' + '1_CB_N_AC_LIGHT1\n')

        for elem in doc.Blocks.item('1_CB_AC_N_SPR'):
            if elem.ObjectName == 'AcDbBlockReference' and elem.EffectiveName == 'CNO':
                coord = elem.InsertionPoint
                elem.Delete()
            else:
                continue
        doc.Blocks.Item('1_CB_AC_N_SPR').InsertBlock(win32com.client.VARIANT(VT_ARRAY | VT_R8, coord), 'CNC', 1.0, 1.0,
                                                     1.0, 0.0)
        doc.SendCommand('ATTSYNC\n' + 'Name\n' + '1_CB_AC_N_SPR\n')

        '''меняем примечание'''
        for i in doc.ModelSpace:
            if i.ObjectName=='AcDbBlockReference' and i.EffectiveName=='FRAME_A3':
                for attr in i.GetAttributes():
                    if attr.TagString=='NOTE':
                        attr.TextString='ПРИМЕЧАНИЕ: Автоматические выключатели предусмотреть с отключающей способностью 6кА.\nТип секционирования щита - 1.\nДополнительные контакты типа S2C-S/H6R перевести в режим аварийного контакта и\nсоединить последовательно для формирования обобщенного сигнала об аварии.'
                    else:
                        continue
    finally:
        doc.Regen(0)
        doc.PurgeAll()
        doc.Close(True)