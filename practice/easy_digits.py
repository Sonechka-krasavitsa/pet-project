def notEasy(element):
    for i in range(2, element - 1):
        if element % i == 0:
            return True
    return False


def makeList(n):
    mlist = [i for i in range(1, int(n) + 1)]
    return mlist


def easyList(element, mlist):
    mlist.remove(element)
    return mlist


i = 0
j = 0
while i < 3:
    n = input('Давай ка ебнем список простых чисел!\nВведи число:\n')
    if n.isdigit():
        mainlist = makeList(n)
        while j < len(mainlist):
            easydigit = notEasy(mainlist[j])
            if easydigit:
                mainlist = easyList(mainlist[j], mainlist)
                j -= 1
            else:
                j += 1
                continue
        print('Вот твой ебучий список простых чисел:\n', mainlist)
        break
    else:
        if i == 2:
            print('Пошри вы нахуй дерфины!')
            break
        else:
            print('Число!! Число надо!!\n')
            i += 1


