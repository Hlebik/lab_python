import random
print ("Добро пожаловать на игру 'Отгадай число'")
print ("Компьютер загадает натуральное число из диапазона от 1 до 100.")
print ("Вам нужно угадать его максиму за 5 попыток.")

#начальные значения
the_number = random.randint (1,100)
guess = int(input("Ваше предположение: "))

while guess != the_number:
    if guess > the_number:
        print ("Меньше...")
    elif:
        print ("Больше..")
        
   
    guess = int(input("\nВаше предположение: "))
    tries += 1

print ("\nПоздравляю! Вам удалось отгадать число!")


