import math


def n(a, b):
    return ((len(a) + len(b)) % 5 + 2) * 2


def f1(size):
    return [i for i in range(0, size, 1)]


def f2(l):
    lopy = list(l)
    lopy.extend((lopy[i] + 1 for i in range(len(lopy))))
    return lopy


# def f3(l):
#     for i in range(int(len(l))):
#         l[len(l):] = [l[i]+1]
#     return l


def f4(l):
    pisa = []
    for i in range(len(l)):
        if l[i] % 3 == 1:
            pisa.append(l[i])
    return pisa


def f5(l):  # ну это когда нашла второе по убыванию число и все такое
    lopy = list(l)
    a = max(lopy)
    i = 0
    while i < len(lopy):
        if lopy[i] == a:
            lopy.remove(lopy[i])
        else:
            i += 1
    return lopy.index(max(lopy))


if __name__ == '__main__':
    print('введите имя')
    name = input()
    print('введите фамилию')
    surname = input()
    l1 = f1(int(n(name, surname)))
    print("task1 ", l1)
    l2 = f2(l1)
    print("task2: ", l2)
    print('task3 ', l2[f5(l2):-1])
    print('task4', f4(l2))
