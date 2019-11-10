import Practice1_1 as valera
import pyautocad

# N = 10
# l = valera.f1(N)
# print(l)
# # l1=valera.f1(6)
# # l[len(l):]=l1
# # print(l)
# l.extend((l[i] + 1 for i in range(int(len(l)))))
# # l=list(valera.f2(l))
# print(l)

# l1 = [4, 4, 4, 2, 2, 4, 2, 1, 4, 3]
# a = max(l1)
# # for i in range(len(l1)):
# i = 0
# while i < len(l1):
#     if l1[i] == a:
#         l1.remove(l1[i])
#     else: i += 1
# print(l1)

s = 'я не знаю права ли я говно'


def f1(s):
    i = 0
    d = {}
    while len(s) - i > 1:
        if s.find(' ') == -1:
            d[s[0:len(s)]] = len(s)
            s = s.replace(s, '')
        else:
            if s[i] == ' ':
                s1 = s[0:i]
                d[s1] = len(s1)
                s = s.replace(s1 + ' ', '')
                i = 0
            else:
                i = i + 1
    return d


def f2(s):
    d = {}
    l = s.split(' ')
    for i in range(len(l)):
        d[l[i]] = len(l[i])
    return d


# print(f2(s))
print(f1(s))
# s = s.replace('я', '')
# print(s)
