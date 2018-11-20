"""Напишите программу, проверяющую
целое число на четность.
Реализовать в виде вызова
собственной функции. """


def fun(number):
    if number%2 == 1:
        return "odd"
    else:
        return "even"

number = int(input("Введите число:"))
print ("Ваше число является:", fun(number))

