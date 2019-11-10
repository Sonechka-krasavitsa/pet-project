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
    return print(row)

def transpose(field):
    return [[row[i] for row in field] for i in range(len(field))]


field_size = input('Укажите размерность игрового поля:\n')
print_field(pull_field(field_size))
print_field(transpose(pull_field(field_size)))