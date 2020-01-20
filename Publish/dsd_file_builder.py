from pathlib import Path
import re

layout_list = ['ЩР-СС.ОФ2.L3.1~1', 'ЩР-СС.ОФ2.L3.1~2', 'ЩР-СС.ОФ2.L3.1~3']
layout_fullname = 'РК-РД-2-ЭМ4.4.01-160-02-ЩР-СС.ОФ2.L3.1~1'
dwg_file_path = 'C:/Users/Sonya/Desktop/python/publish/РК-РД-2-ЭМ4.4.01-160-02.dwg'
file_name = 'РК-РД-2-ЭМ4.4.01-160-02'
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
    reg_exp = r'(?P<fullmatch>\${(?P<marker>\w{1,})})'
    match_list = re.findall(reg_exp, text)
    fullmatch_list = [match_list[i][0] for i in range(len(match_list))]
    marker_list = [match_list[j][1] for j in range(len(match_list))]
    return fullmatch_list, marker_list


dsd_temporary_file.touch()
# dsd_temporary_file.write_text("[DWF6Version]\nVer=1\n[DWF6MinorVersion]\nMinorVer=1\n")
# dsd_temporary_file.write_text(dsd_temporary_file.read_text().replace('DWG', 'huy'))
fullmatch_list = get_marker(sheet_info_block.read_text())[0]
marker_list = get_marker(sheet_info_block.read_text())[1]
print(fullmatch_list)
print(marker_list)

