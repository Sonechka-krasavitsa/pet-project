from typing import List, Any
import numpy as np


def pull_field(razmer):
    if not razmer.isdigit():
        raise ValueError
    razmer = int(razmer)
    field = [[0 for i in range(razmer)] for j in range(razmer)]
    a = 1
    for i in range(razmer):
        for j in range(razmer):
            field[i][j] = a
            a += 1
    return field


def print_field(field_func):
    row = ''
    for i in range(len(field_func)):
        for j in range(len(field_func[i])):
            element = field_func[i][j]
            row = row + str(element) + ' '
        row = row + '\n'
    return row


def fill_field(adress, field, filling):
    if not adress.isdigit():
        raise ValueError
    if int(adress) > len(field) ** 2:
        raise SystemError
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == int(adress):
                field[i][j] = filling
                return field
    raise IndexError


def daun(func, adress, field):
    try:
        field = func(adress, field, 'X' if adress == krestik else 'O')
    except IndexError:
        print('Данная ячейка занята, блядь')
    except ValueError:
        print('Вводи целое число, идиот')
    except SystemError:
        print('Такого адреса нет! Вводи от 1 до', len(field) ** 2)
    return field


def win_check_rows(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if j == 0:
                continue
            else:
                if j == len(field[i]) - 1:
                    if field[i][j] == field[i][j - 1]:
                        return True
                    else:
                        break
                if field[i][j] == field[i][j - 1]:
                    continue
                else:
                    break
    return False


def win_check_column(field):
    for j in range(len(field[0])):
        for i in range(len(field)):
            if i == 0:
                continue
            else:
                if i == len(field) - 1:
                    if field[i][j] == field[i - 1][j]:
                        return True
                    else:
                        break
                if field[i][j] == field[i - 1][j]:
                    continue
                else:
                    break
    return False


def win_check_diagonal(field):
    listDiagonal = []
    for i in range(len(field)):
        listDiagonal.append(field[i][i])
    for i in range(len(listDiagonal)):
        if i == 0:
            continue
        else:
            if i == len(listDiagonal) - 1:
                if listDiagonal[i] == listDiagonal[i - 1]:
                    return True
                else:
                    break
            else:
                if listDiagonal[i] == listDiagonal[i - 1]:
                    continue
                else:
                    break
    return False



field_size = input('Укажите размерность игрового поля:\n')
try:
    main_field = pull_field(field_size)
    print(print_field(main_field))
except ValueError:
    print('Ты шо даун?!')

for i in range(int(field_size) ** 2 - 1):
    krestik = input('Куда поставим крестик?\n')
    daun(fill_field, krestik, main_field)
    if win_check_diagonal(main_field):
        print('Охуеть победили крестики!\n' + print_field(main_field))
        break
    else:
        print(print_field(main_field))
    nolik = input('Куда поставим нолик?\n')
    daun(fill_field, nolik, main_field)
    if win_check_diagonal(main_field):
        print('Охуеть победили нолики!\n' + print_field(main_field))
        break
    else:
        print(print_field(main_field))
