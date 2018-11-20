def my_max (a,b):
    if a >= b:
        return a
    elif  b>= a:
        return b
    
a = int(input("Введите число 1:"))
b = int(input("Введите число 2:"))
print(my_max(a, b))
