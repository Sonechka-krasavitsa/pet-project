import win32com.client as win32
from tkinter import filedialog
from pathlib import Path
import re

appdir = Path.cwd()
dsd_template_file = appdir / "template.dsd"
sheet_info_block = appdir / "sheet_info_block.dsd"
dsd_temporary_file = appdir / "tmp.dsd"


def get_marker(text):
    '''
    регулярное выражение, которое ищет маркеры вида ${xxx_xxx} в тексте шаблонов
    '''
    reg_exp = r'\${\w{1,}}'
    return re.findall(reg_exp, text)


def sheet_dict(layout_name, file_name, dwg_file_path):
    '''
    функция создает словарь с информацией о листах. ключи - маркеры из шаблона sheet_info_block.dsd,
    значения - информация, которую подставляем вместо маркера
    '''
    sheet_dict = {}
    sheet_dict['${layout_fullname}'] = re.sub(r'\.\w{3}', r'', file_name) + '-' + layout_name
    sheet_dict['${dwg_file_path}'] = dwg_file_path
    sheet_dict['${layout_name}'] = layout_name
    return sheet_dict


def setting_dict(pdf_target_folder, file_name, dsd_temporary_file):
    '''
    функция создает словарь с информацией о печати. ключи - маркеры из шаблона template.dsd,
    значения - информация, которую подставляем вместо маркера
    '''
    setting_dict = {}
    setting_dict['${pdf_file_path}'] = pdf_target_folder + '\\' + re.sub(r'\.dwg', r'.pdf', file_name)
    setting_dict['${target_folder}'] = pdf_target_folder
    setting_dict['${dsd_file_path}'] = str(dsd_temporary_file)
    return setting_dict


def path_correction(path_iter):
    new_path = []
    for path in path_iter:
        new_path.append(path.replace('/', '\\'))
    return new_path


if __name__ == '__main__':

    '''Запрашиваем у пользователя файлы для паблиша и папку, куда сохраняем PDF'''
    tmp_file_list = filedialog.askopenfilenames()
    tmp_pdf_target_folder = filedialog.askdirectory()

    '''Меняем / на \\'''
    file_list = path_correction(tmp_file_list)
    pdf_target_folder = tmp_pdf_target_folder.replace('/', '\\')

    app = win32.gencache.EnsureDispatch("AutoCAD.Application")
    for i in file_list:
        '''Открываем файл, берем информацию о листах и имя файла'''
        doc = app.Documents.Open(i, False)
        file_name = doc.Name
        all_layout_info = doc.Layouts
        layout_list = []
        for j in all_layout_info:
            if j.Name == "Model":
                continue
            else:
                layout_list.append(j.Name)

        '''Генерируем файл dsd'''
        '''Собираем блок с информацией по листам'''
        main_text = "[DWF6Version]\nVer=1\n[DWF6MinorVersion]\nMinorVer=1"
        marker_list = get_marker(sheet_info_block.read_text())
        for j in range(len(layout_list)):
            sheet_info_dict = sheet_dict(layout_list[j], file_name, i)
            tmp_text = sheet_info_block.read_text()
            for k in range(len(marker_list)):
                tmp_text = tmp_text.replace(marker_list[k], sheet_info_dict[marker_list[k]])
            main_text = main_text + '\n' + tmp_text

        '''Собираем блок с информацией по печати'''
        setting_info_dict = setting_dict(pdf_target_folder, file_name, dsd_temporary_file)
        tmp_text = dsd_template_file.read_text()
        marker_list = get_marker(tmp_text)
        for j in range(len(marker_list)):
            tmp_text = tmp_text.replace(marker_list[j], setting_info_dict[marker_list[j]])
        main_text = main_text + '\n' + tmp_text
        dsd_temporary_file.touch()
        dsd_temporary_file.write_text(main_text)

        '''Посылаем на печать файл'''
        doc.SetVariable('FILEDIA', 0)
        doc.SendCommand("-PUBLISH\n" + str(dsd_temporary_file) + '\n')
        doc.SetVariable('FILEDIA', 1)
        doc.Close(False)
