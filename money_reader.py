#def money_reader():

import csv
import operator
money = {}
a=[]
with open('opendata.csv', encoding='cp1251') as csvfile:
    money_reader = csv.reader(csvfile, delimiter=',') # delimiter по умолчанию ','
    for row in money_reader:
        if row[0] == 'Количество заявок на потребительские кредиты':
            if '2017' in row[2]:
                if row[1] not in money:
                    money[row[1]] = [row[3]]
                else:
                   money[row[1]].append(row[3])
                   



for key, value in money.items():
    money[key] = sum(map(int, value))
money.pop('Россия')
print(max(money.items(), key=operator.itemgetter(1)))

