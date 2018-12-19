import math

def f(x):
    return "Ответ: {PI:.{num}f}".format(PI = math.pi, num = x)


x = int(input('>> '))
print(f(x))

