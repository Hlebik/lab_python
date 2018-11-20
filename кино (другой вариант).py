print ("Программа для подсчета стоимости билетов в кино.")
movie = input ("Выберите фильм: ")
date = input ("Выберите дату: ")
time = input ("Выберите время: ")
ticket_amount = int(input ("Укажите количество билетов: "))

def full_price(movie, ticket_amount):
    if movie == "Пятница":
        if time == "12 часов":
            return 250* ticket_amount
        elif time == "16 часов":
            return 350*ticket_amount
        elif time == "20 часов":
            return 450*ticket_amount
    elif movie == "Чемпионы":
        if time == "10 часов":
            return 250* ticket_amount
        elif time == "13 часов":
            return 350*ticket_amount
        elif time == "16 часов":
            return 350*ticket_amount
    elif movie == "Пернатая банда":
        if time == "10 часов":
            return time*ticket_anount
        elif time == "14 часов":
            return time*ticket_amount
        elif time == "18 часов":
            return time*ticket_amount

