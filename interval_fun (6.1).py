"""Найдите сумму всех значений функции
y(x) = x**2 + 3
на интервале от 10 до 30 с шагом 2"""

sum=0
for i in range(10,30,2):
    sum+=i**2+3
print(sum)


