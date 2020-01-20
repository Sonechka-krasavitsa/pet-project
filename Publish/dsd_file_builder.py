from pathlib import Path
import re

layout_list = ['ЩР-СС.ОФ2.L3.1~1', 'ЩР-СС.ОФ2.L3.1~2', 'ЩР-СС.ОФ2.L3.1~3']
dwg_file_path = 'C:/Users/Sonya/Desktop/python/publish/РК-РД-2-ЭМ4.4.01-160-02.dwg'
file_name = 'РК-РД-2-ЭМ4.4.01-160-02.dwg'
dsd_target_folder = 'C:/Users/Sonya/Desktop/python/publish/'
pdf_target_folder = 'C:/Users/Sonya/Desktop/python/publish/PDF/'
appdir = Path.cwd()
dsd_template_file = appdir / "template.dsd"
sheet_info_block = appdir / "sheet_info_block.dsd"
dsd_temporary_file = appdir / "tmp.dsd"


def get_marker(text):
    '''
    регулярное выражение, которое ищет маркеры вида ${xxx_xxx} в тексте
    группа marker возвращает имя параметра xxx_xxx
    '''
    reg_exp = r'(\${(\w{1,})})'
    match_list = re.findall(reg_exp, text)
    fullmatch_list = [match_list[i][0] for i in range(len(match_list))]
    marker_list = [match_list[j][1] for j in range(len(match_list))]
    return fullmatch_list, marker_list


def sheet_dict(layout_name, file_name, dwg_file_path):
    sheet_dict = {}
    sheet_dict['${layout_fullname}'] = re.sub(r'\.dwg', r'', file_name) + '-' + layout_name
    sheet_dict['${dwg_file_path}'] = dwg_file_path
    sheet_dict['${layout_name}'] = layout_name
    return sheet_dict


dsd_temporary_file.touch()
# dsd_temporary_file.write_text("[DWF6Version]\nVer=1\n[DWF6MinorVersion]\nMinorVer=1\n")
# dsd_temporary_file.write_text(dsd_temporary_file.read_text().replace('DWG', 'huy'))
fullmatch_list = get_marker(sheet_info_block.read_text())[0]
marker_list = get_marker(sheet_info_block.read_text())[1]
print(fullmatch_list)
print(marker_list)
layout_name = 'ЩР-СС.ОФ2.L3.1~1'
sheet_dict = sheet_dict(layout_name, file_name, dwg_file_path)
print(sheet_dict)
print(len(sheet_dict))
for i in range(len(fullmatch_list)):
    sheet_info_block.write_text(
        sheet_info_block.read_text().replace(fullmatch_list[i], sheet_dict[fullmatch_list[i]]))
