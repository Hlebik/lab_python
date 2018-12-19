"""Написать программу, вычисляющую значение
функции (на вход подается вещественное число):"""


from math import sin
def fun1(x):
    if 0.2<=x<=0.9:
        return sin(x)
    else:
        return 1

x=float(input("Введите значение:"))
print ("Значение равно:", fun1(x))










"""def fun_1 (math):
    if -2.4<=math<=5.7:
        return math**2
    else:
        return 4

    
math = float(input("Введите значение:"))
print ("значение равно:", fun_1(math))"""
