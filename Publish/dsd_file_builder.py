from pathlib import Path
import re

layout_list = ['ЩР-СС.ОФ2.L3.1~1', 'ЩР-СС.ОФ2.L3.1~2', 'ЩР-СС.ОФ2.L3.1~3']
dwg_file_path = 'C:/Users/Sonya/Desktop/python/publish/РК-РД-2-ЭМ4.4.01-160-02.dwg'
file_name = 'РК-РД-2-ЭМ4.4.01-160-02.dwg'
pdf_target_folder = 'C:/Users/SoAlekseeva/PycharmProjects/pet-project/Publish'
appdir = Path.cwd()
dsd_template_file = appdir / "template.dsd"
sheet_info_block = appdir / "sheet_info_block.dsd"
dsd_temporary_file = appdir / "tmp.dsd"


def get_marker(text):
    '''
    регулярное выражение, которое ищет маркеры вида ${xxx_xxx} в тексте
    '''
    reg_exp = r'\${\w{1,}}'
    return re.findall(reg_exp, text)


def sheet_dict(layout_name, file_name, dwg_file_path):
    sheet_dict = {}
    sheet_dict['${layout_fullname}'] = re.sub(r'\.\w{3}', r'', file_name) + '-' + layout_name
    sheet_dict['${dwg_file_path}'] = dwg_file_path
    sheet_dict['${layout_name}'] = layout_name
    return sheet_dict


def setting_dict(pdf_target_folder, file_name, dsd_temporary_file):
    sheet_dict = {}
    sheet_dict['${pdf_file_path}'] = pdf_target_folder+'/'+ re.sub(r'\.dwg', r'.pdf', file_name)
    sheet_dict['${target_folder}'] = pdf_target_folder
    sheet_dict['${dsd_file_path}'] = dsd_temporary_file.as_posix()
    return sheet_dict


'''Собираем блок с информацией по листам'''
main_text = "[DWF6Version]\nVer=1\n[DWF6MinorVersion]\nMinorVer=1"
marker_list = get_marker(sheet_info_block.read_text())
for j in range(len(layout_list)):
    sheet_info_dict = sheet_dict(layout_list[j], file_name, dwg_file_path)
    tmp_text = sheet_info_block.read_text()
    for i in range(len(marker_list)):
        tmp_text = tmp_text.replace(marker_list[i], sheet_info_dict[marker_list[i]])
    main_text = main_text + '\n' + tmp_text

'''Собираем блок с информацией по печати'''
setting_info_dict = setting_dict(pdf_target_folder, file_name, dsd_temporary_file)
tmp_text = dsd_template_file.read_text()
marker_list = get_marker(tmp_text)
for i in range(len(marker_list)):
    tmp_text = tmp_text.replace(marker_list[i], setting_info_dict[marker_list[i]])
main_text = main_text + '\n' + tmp_text
dsd_temporary_file.touch()
dsd_temporary_file.write_text(main_text)
