def f1(n):
    n = int(n)
    i = 1
    l = 1
    while l < n:
        l = l + 2 ** i
        i += 1
    return i


i = 0
while i < 3:
    n = input('Введи километры\n')
    if n.isdigit():
        print(f1(n))
        break
    else:
        if i == 2:
            print('Да пошел ты..')
        else:
            print('ты долбоящер? нужно число!')
    i += 1

    # def getDays(n):
#     try:
#         n = int(n)
#     except ValueError: raise
#     a = 1
#     l = 1
#     while l < n:
#         l = l + 2 ** a
#         a += 1
#     return a
# i=1
# def getDaysInput():
#     global i
#     n = input('Введи километры\n')
#     try:
#         print(getDays(n))
#     except (ValueError):
#         print('Ну ты число вводи, хули?!')
#         i+=1
#         if i<=3: getDaysInput()
#         else: print('Ну ты и дурак!')
#
# getDaysInput()
