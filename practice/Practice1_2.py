# print('введите число')
# n = int(input())


print('введите строку')
s = input()


def f1(n, s):
    for i in range(n):
        print(s)


def f2(n):
    i = 1
    while i <= n:
        print("=" * i)
        i = i + 1


def f3(s):
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]] = d[s[i]] + 1
        else:
            d[s[i]] = 1
    return d


def f4(s):
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


def f5(s):
    d = {}
    l = s.split(' ')
    for i in range(len(l)):
        d[l[i]] = len(l[i])
    return d


# f1(n, s)
# f2(n)
print(f3(s))
print(f4(s))
print(f5(s))
