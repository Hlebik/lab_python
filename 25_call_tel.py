def price(kod,time):
    if kod == 343:
        return time * 15
    elif kod == 381:
        return time * 18
    elif kod == 473:
        return time * 13
    elif kod == 485:
        return time * 11
    else:
        return("Введите корректный код: ")

kod = int(input("Введите код города: "))
time = int(input("Введите длительность переговоров: "))
print("Стоимость разговора составляет: ", price(kod,time))
