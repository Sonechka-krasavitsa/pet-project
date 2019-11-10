# import math
# # a=20.4
# # for i in range(21):
# #     if i==0:
# #         continue
# #     print(str(i)+' '+str(a*i))
# # d1={"Valera":"piskotryas","paddy":"norm", "Sonechka":"norm"}
# # "Valera" in d1
# # d1.get("Valera")
# # def huuy(n):
# #     if n==0:
# #         return 0
# #     elif n==1:
# #         return 1
# #     elif n==2:
# #         return 1
# #     else:
# #         return huuy(n-1)+huuy(n-2)
# # print(huuy(5))
# #
# # def fuck(n):
# #     if n==0:
# #         return 0
# #     elif n==1:
# #         return 1
# #     else:
# #         return n*fuck(n-1)
# # print(fuck(5))
# # print("введите число")
# # a=str(input())
# # print("введите количество")
# # n=int(input())
# # b=a+' '
# # for i in range(n-1):
# #     b=b+str(a)+" "
# #     continue
# # print(b)
# #
# # for i in range(36):
# #     if i>=20:
# #         print(i)
# a = 10
# print('vvedi huuy')
# b=int(input())
#
# def chlen():
#     if b<=a:
#         print('pidor tupoy, vvedi bolshe 10')
#         print('budeshh vvodit? Y/N')
#         c=input()
#         if c=='Y': chlen()
#     else:
#         print('nu i poshel nahuuy')
#     while a<= b:
#         print(a ** 2)
#         a = a + 1
# chlen()

c='Y'

def vvod():
        print('input number:')
        number = int(input())
        if number > 10:
            print(number**2)
        else:
            print("number shall be more then 10")

while c=='Y':
    vvod()
    print('would you like play again?')
    c = input()
