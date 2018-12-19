"""Задан список слов. Необходимо выбрать из него случайное. Из
выбранного случайного слова случайно выбрать букву и попросить
пользователя ее угадать."""


"""import random

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
    print("Oh no, boy u better study harder")"""
    

import random
while True:
    word_ran = {'dog':'собака', 'cat':'кошка', 'bird':'птица', 'tiger': 'тигр', 'sea lion' : 'морской котик'} 
    a = word_ran
    lst = list(a)
    b = random.choice(lst)
    print (b)
    guess = str(input("Угадай слово:"))
    if guess == word_ran[b]:
        print ("Вы угадали слово")
    else:
        print ("Попробуйте еще раз")
