"""Напишите программу для определения стоимости билетов в кино с учетом скидок.
Льготы
При покупке билетов за день до сеанса: скидка 5%
Вы можете купить билет со скидкой 20%. Для этого нужно собрать компанию не менее 20
человек.

Порядок действий:
1. выбрать фильм
2. выбрать дату (сегодня, завтра)
3. выбрать время
4. указать количество билетов
5. определить стоимость

Фильм «Пятница»,сеансы:
12 часов – 250 руб, 16 – 350 руб, 20 – 450 руб.

Фильм «Чемпионы»,сеансы:
10 часов – 250 руб, 13 – 350 руб, 16 – 350 руб.

Фильм «Пернатая банда»,сеансы:
10 часов – 350 руб, 14 – 450 руб, 18 – 450 руб.


movie
date
time
amount
price"""

print ("Программа для подсчета стоимости билетов в кино.")
movie = input ("Выберите фильм: ")
date = input ("Выберите дату: ")
time = input ("Выберите время: ")
ticket_amount = int(input ("Укажите количество билетов: "))
if movie == "Пятница":
    if date == "сегодня":
        if time == "12 часов":
            if ticket_amount>=20:
                print ("Цена билета:", (250*ticket_amount)*0.8)
            else:
                print ("Цена билета:", (250*ticket_amount))
        elif time == "16 часов":
            if ticket_amout>=20:
                print ("Цена билета:", (350*ticket_amount)*0.8)
            else:
                print ("Цена билета:", (350*ticket_amount))
        elif time == "20 часов":
            if ticket_amount>=20:
                print ("Цена билета:", (450*ticket_amount)*0.8)
            else:
                print ("Цена билета:", (450*ticket_amount))
    else:
        if time == "12 часов":
            if ticket_amount>=20:
                print ("Цена билета:", (250*ticket_amount)*0.8*0.95)
            else:
                print ("Цена билета:", (250*ticket_amount)*0.95)
        elif time == "16 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (350*ticket_amount)*0.8*0.95)
            else:
                print ("Цена билета:", (350*ticket_amount)*0.95)
        elif time == "20 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (450*ticket_amount)*0.8*0.95)
            else:
                print ("Цена билета:", (450*ticket_amount)*0.95)
        
        
elif movie == "Чемпионы":
    if date=="сегодня":
        if time == "10 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (250*ticket_amount)*0.8)
            else:
                print ("Цена билета:", (250*ticket_amount))
        elif time == "13 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (350*ticket_amount)*0.8)
            else:
                print ("Цена билета:", (350*ticket_amount))
        elif time == "16 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (350*ticket_amount)*0.8)
            else:
                print ("Цена билета:", (350*ticket_amount))
    else:
        if time == "10 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (250*ticket_amount)*0.8*0.95)
            else:
                print ("Цена билета:", (250*ticket_amount)*0.95)
        elif time == "13 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (350*ticket_amount)*0.8*0.95)
            else:
                print ("Цена билета:", (350*ticket_amount)*0.95)
        elif time == "16 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (350*ticket_amount)*0.8*0.95)
            else:
                print ("Цена билета:", (350*ticket_amount)*0.95)
        
elif movie == "Пернатая банда":
    if date=="сегодня":
        if time == "10 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (350*ticket_amount)*0.8)
            else:
                print ("Цена билета:", (350*ticket_amount))
        elif time == "14 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (450*ticket_amount)*0.8)
            else:
                print ("Цена билета:", (450*ticket_amount))
        elif time == "18 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (450*ticket_amount)*0.8)
            else:
                print ("Цена билета:", (450*ticket_amount))
    else:
        if time == "10 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (350*ticket_amount)*0.8*0.95)
            else:
                print ("Цена билета:", (350*ticket_amount)*0.95)
        elif time == "14 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (450*ticket_amount)*0.8*0.95)
            else:
                print ("Цена билета:", (450*ticket_amount)*0.95)
        elif time == "18 часов":
            if ticket_amount >=20:
                print ("Цена билета:", (450*ticket_amount)*0.8*0.95)
            else:
                print ("Цена билета:", (450*ticket_amount)*0.95)
        

    
                
                



