'''Корректировка штампа:
1. Меняем ИД на РД
2. Меняем дату
3. Корректируем общее количесвто листов'''

import win32com.client
from tkinter import filedialog


tmp_file_list = filedialog.askopenfilenames()

app = win32com.client.Dispatch("AutoCAD.Application")
for file in tmp_file_list:
    try:
        doc = app.Documents.Open(file, False)

        '''Меняем ИД на РД'''
        text_dict = {elem.Handle: elem.TextString for elem in doc.Blocks.item('FRAME_TITLE') if
                     elem.ObjectName == 'AcDbText'}
        for key, value in text_dict.items():
            if value == 'ИД':
                text_dict[key] = value.replace('ИД', 'РД')
                for elem in doc.Blocks.item('FRAME_TITLE'):
                    if elem.Handle == key:
                        elem.TextString = text_dict[key]
            else:
                continue

        '''корректируем количество листов и дату в штампе'''
        block_list = [x.EffectiveName for x in doc.ModelSpace if
                      x.ObjectName == 'AcDbBlockReference' and x.EffectiveName == 'FRAME_A3']
        block_attr_list = [i.GetAttributes() for i in doc.ModelSpace if
                           i.ObjectName == 'AcDbBlockReference' and i.EffectiveName == 'FRAME_TITLE']
        for attr in block_attr_list:
            for i in attr:
                if i.TagString == "SUMSHEET":
                    i.TextString = len(block_list) + 1
                if i.TextString == 'Откорректировано подключение дополнительных контактов':
                    i.TextString = 'Откорректирована вводная линия'
                if i.TextString == '16.08.19':
                    i.TextString = '02.03.20'
                else:
                    continue

        '''меняем дату на остальных листах'''
        for i in doc.ModelSpace:
            if i.ObjectName == 'AcDbBlockReference' and i.EffectiveName == 'FRAME_A3':
                for attr in i.GetAttributes():
                    if attr.TextString == '16.08.19':
                        attr.TextString = '02.03.20'
                    else:
                        continue

        '''меняем %%% на %'''
        for i in doc.ModelSpace:
            if i.ObjectName == 'AcDbBlockReference':
                for attr in i.GetAttributes():
                    if attr.TagString == 'LN02':
                        attr.TextString = attr.TextString.replace('%%%', '%')
            else:
                continue

    finally:
        doc.regen(0)
        doc.Close(True)
        text_dict.clear()

