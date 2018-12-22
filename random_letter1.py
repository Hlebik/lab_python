"""Задан список слов. Необходимо выбрать из него случайное. Из
выбранного случайного слова случайно выбрать букву и попросить
пользователя ее угадать."""


import random
while True:
    word_ran = {'dog': 'собака', 'cat': 'кошка', 'bird': 'птица',
                'tiger': 'тигр', 'sea lion': 'морской котик'}
    a = word_ran
    lst = list(a)
    b = random.choice(lst)
    print(b)
    guess = str(input("Угадай слово:"))
    if guess == word_ran[b]:
        print("Вы угадали слово")
    else:
        print("Попробуйте еще раз")
