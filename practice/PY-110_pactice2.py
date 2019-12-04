# Lambda практика

import random


def lambda_foo1():
    spisok = [tuple(random.randint(1, 100) for i in range(2)) for i in range(10)]
    sorted_spisok = sorted(spisok, key=lambda spisok: spisok[1], reverse=True)
    return print("Вот твой блядский список\n", spisok, "\n А вот тот же список отсортированный\n", sorted_spisok)


def lambda_foo2():
    print(sorted(input("Введи какое-нибудь предложение\n").split(), key=len, reverse=True))


def zamykasha(x):
    # пример замыкания на лямбда функции
    y = 3
    return lambda z: x - y + z


schet = zamykasha(3)


# def generator_1(sentence):
#     print(sentence.split())
#     return ()
#
#
# sentence = input("Введи предложение\n")
# print(type(sentence))
# for i in range(len(sentence.split())):
#     print(generator_1(sentence))
#     print(next(generator_1(sentence)))
def generator_1():
    s = "мы пойдем на футбол"
    gen = (i for i in s.split())
    for i in range(len(s.split())):
        print(next(gen))


# Корутина
def counter(start):
    n = start
    while True:
        new_start = yield n
        if new_start is not None:
            n=new_start
        else:
            n += 1

# def f

x=counter(100)
for i in range(10):
    print(next(x))






