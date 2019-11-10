import random

pc_digit = random.randrange(1, 100, 1)
print(type(pc_digit))
i = 0


def user_guess():
    global i
    i += 1
    user_variant = input('Введи в меня..число:\n')
    return user_variant


def guess_digit(user_variant):
    if not user_variant.isdigit():
        raise ValueError
    user_variant = int(user_variant)
    global pc_digit, i
    if user_variant == pc_digit:
        print("А ты хорош! Загаданное число: ", pc_digit, "\nОтгадал с ", i, " раза")
    elif user_variant < pc_digit:
        print("Загаданное число больше, чем ты начирикал тут")
        guess_digit(user_guess())
    elif user_variant > pc_digit:
        print("Загаданное число меньше, чем ты начирикал тут")
        guess_digit(user_guess())


print("Ну???")
n = user_guess()
guess_digit(n)
