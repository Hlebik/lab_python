def fun(number):
    if number%2 == 1:
        return "odd"
    else:
        return "even"

number = int(input("Введите число:"))
print("Ваше число является:", fun(number))
