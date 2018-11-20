print ("Программа для подсчета стоимости билетов в кино.")
movie = input ("Выберите фильм: ")
date = input ("Выберите дату: ")
time = input ("Выберите время: ")
ticket_amount = int(input ("Укажите количество билетов: "))

def full_price_1(movie, ticket_amount):
tmp_price= full_price_1(movie, ticket_amount)
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
            return 350*ticket_amount
        elif time == "14 часов":
            return 450*ticket_amount
        elif time == "18 часов":
            return 450*ticket_amount

print ("Стоимость билетов составляет: ", full_price_1(movie, ticket_amount))


def full_price_2(date, tmp_price, ticket_amount):
    if date == "завтра":
        if ticket_amount>=20:
            return full_price_1*0.8*0.95
    elif date == "сегодня":
        if ticket_amount>=20:
            return full_price_1*0.8
    else:
        if ticket_amount <=20:
            return full_price_1

print ("Стоимость билетов составляет: ", full_price_2(date,tmp_price,ticket_amount))

        
        

