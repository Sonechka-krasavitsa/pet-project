import win32com.client
from pythoncom import VT_R8, VT_ARRAY, VT_I2, VT_VARIANT, com_error
import win32api
import re


def block_input(prompt, block_name):
    '''Вставка блока в AutoCad пользователем, по указанной курсором точке'''
    doc.Utility.Prompt(prompt)
    coord = doc.Utility.GetPoint()
    point = win32com.client.VARIANT(VT_ARRAY | VT_R8, coord)
    return doc.ModelSpace.InsertBlock(point, block_name, 1.0, 1.0, 1.0, 0.0)


def counter(start):
    '''Счетчик с заданваемым стартовым значением и с шагом 1'''
    n = start
    while True:
        n += 1
        yield n


def filtered_block_set(set_name, block_name):
    """сет из блоков, фильтр по имени блока
    set_name - str
    block_name - str"""
    sel_set = doc.SelectionSets.Add(set_name)
    FilterType = win32com.client.VARIANT(VT_ARRAY | VT_I2, [2])
    FilterData = win32com.client.VARIANT(VT_ARRAY | VT_VARIANT, [block_name])
    sel_set.Select(5, None, None, FilterType, FilterData)
    return sel_set


def rev_num_filter(global_rev_num, elem):
    '''Фильтр атрибутов ревизий по введенной пользователем глобальной ревизии'''
    reg_exp = r'(0|){}\.'.format(global_rev_num)
    if re.match(reg_exp, elem):
        return int(re.sub(reg_exp, r'', elem))


app = win32com.client.Dispatch("AutoCAD.Application")
doc = app.ActiveDocument

global_rev_num = 5

if __name__ == "__main__":
    try:
        new_block = block_input("бахни", "RevTag")
        sel_set = filtered_block_set("RevTagSet", "RevTag")

        print(len(sel_set))
        '''Удали потом это. Контролируем количество выбранных блоков'''

        attr_set = []
        for i in sel_set:
            attr_set.append(i.GetAttributes())

        rev_num_temp_list = []
        for i in attr_set:
            for j in i:
                rev_num_temp_list.append(j.TextString)

        rev_num_list = []
        for i in rev_num_temp_list:
            if rev_num_filter(global_rev_num, i):
                rev_num_list.append(rev_num_filter(global_rev_num, i))

        print(rev_num_list)

        for i in new_block.GetAttributes():
            if i.TagString == 'REVNUM':
                i.TextString = str(global_rev_num) + '.' + str(max(rev_num_list) + 1)

        for i in counter(max(rev_num_list) + 1):
            extra_block = block_input("Еще?", "RevTag")
            for j in extra_block.GetAttributes():
                if j.TagString == 'REVNUM':
                    j.TextString = str(global_rev_num) + '.' + str(i)


    except com_error as error:
        errnumber = error.excepinfo[-1]
        if errnumber == -2147352567:
            print('нажат esc')

    finally:
        sel_set.Delete()
