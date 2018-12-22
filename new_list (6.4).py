"""Напишите программный код, который будет
создавать новый список, содержащий в
качестве элементов квадратные корни всех
чисел из списка
[2, 4, 9, 16, 25]:
1) на основе цикла for
2) на основе функции map
3) в виде генератора списка"""

from math import sqrt
sum = 0
lst = [2, 4, 9, 16, 25]
lst_2 = []
for x in lst:
    lst_2.append(sqrt(x))
print(lst_2)

lst_3 = list(map(lambda x: sqrt(x), lst))
print(lst_3)

lst_4 = [sqrt(x) for x in lst]
print(lst_4)
