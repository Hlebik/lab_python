def fun_fact(number):
    if number == 3.0:
        return "Li-Литий"
    elif number == 17.00:
        return "Cl=Хлор"
    elif number == 25.00:
        return "Mn-Магний"
    elif number == 80.00:
        return "Hg- Ртуть"
    else:
        return "Неверные исходные данные"


number = int(input("Введите номер химического элемента: "))
print("Химический элемент: ", fun_fact(number))
        

        
