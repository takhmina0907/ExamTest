import random

print('''
Привет! Давай играть в угадай число!
Твоя задача угадать число от 1 до 10! Помни у тебя всего 3 попытки.
''')

comp = random.randint(1,10)
tries = 3

while tries > 0:
    me = int(input("Твое число: "))

    if comp > me:
        print("Введи число больше!")
    elif comp < me:
        print("Введи число меньше!")
    else:
        print("Победа!")
        break
    tries -=1

    if tries == 0:
        print ("Ты проиграл! Я загадал число:", comp)