"""Задан список слов. Необходимо выбрать из него случайное. Из
выбранного случайного слова случайно выбрать букву и попросить
пользователя ее угадать."""

import random
fun = ['самовар','весна','лето']
a=random.choice(fun)
lst = list(a)
b=random.choice(lst)
i = a.index(b)
lst[i]= "?"
print("выводим на экран:", ''.join(lst))
guess = str(input("Give it a try:"))
if guess == b:
    print("Damn boy u did well")
else:
    print("Oh no, boy u better study harder")
