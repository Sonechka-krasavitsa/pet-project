import win32com.client
from pythoncom import VT_R8, VT_ARRAY, VT_I2, VT_VARIANT, com_error
import numpy as np
import win32api
from rev_tag import block_input, filtered_block_set
import re


def rev_num_filter(elem):
    global global_rev_num '''глобальная переменная тут - говно собачье. попробуй избавиться.'''
    reg_exp = r'(0|){}\.'.format(global_rev_num)
    if re.match(reg_exp, elem):
        return True


# print(rev_num_filter())
#
# if rev_num_filter() is not None:
#     print("работает")
# else:
#     print("писька")

# app = win32com.client.Dispatch("AutoCAD.Application")
# doc = app.ActiveDocument
#
# new_block = block_input("бахни", "RevTag")
# sel_set = filtered_block_set("Re44v656564Ta56gSet", "RevTag")
#
# attr_set = []
# for i in sel_set:
#     attr_set.append(i.GetAttributes())
#
# rev_num_list = []
# for i in attr_set:
#     for j in i:
#         rev_num_list.append(j.TextString)
#
# print(rev_num_list)

global_rev_num = 3
rev_num_list = ['03.45', '3.45', '05.45']

rev_num_list1 = filter(rev_num_filter, rev_num_list)
print([i for i in rev_num_list1])
