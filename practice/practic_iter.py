import itertools

'''задачка1'''
mainList = (i for i in itertools.count(1, 1))


def square(x):
    return x ** 2


def chetny(x):
    if x % 2 == 0:
        return x


# mainList1 = map(square, mainList)
# mainList2 = filter(chetny, mainList1)

# if __name__ == '__main__':
#     for i in range(20):
#         print(next(mainList2))

'''задачка2'''
stroka = input('Введи строку:\n')
print('Длина строки ', len(stroka) - 1)
adress = []
for i in range(3):
    if i == 0:
        adress.extend(input('Введи 3 индекса от 0 до длины строки:\n'))
    else:
        adress.extend(input('еще\n'))


def indexStroka(stroka, adress):
    resultList = []
    for i in range(len(adress)):
        resultList.extend(stroka[int(adress[i])])
    return resultList


print(indexStroka(stroka,adress))


finalStroka2=[stroka[int(x)] for x in adress]
print(finalStroka2)
print(list(enumerate(stroka,0)))