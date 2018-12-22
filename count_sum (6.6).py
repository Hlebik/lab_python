"""Дано число, введенное с клавиатуры.
Определить сумму квадратов нечетных
цифр в числе."""


s = str(input("Введите число с клавиатуры: "))
total = 0
for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        continue
    total = total + int(s[i])


print("сумма цифр:", total)
