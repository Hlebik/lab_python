
import random
print ("\tДобро пожаловать в игру 'Отгадай число'!")
print ("\nЯ загадал число из диапозона от 1 до 100.")
print ("Постарайтесь отгадать его за минимальное число попыток.\n")

the_number = random.randint (1, 4)
guess = int (input("Ваше предложение: "))
tries = 1
while guess != the_number:
    if guess > the_number:
        print ("Меньше...")
    else:
        print ("Больше...")
    guess = int (input("Ваше предложение.."))
   
print ("Вам удалось отгадать число! Это и в самом деле ", the_number)




the_number = random.randint (1, 4)
guess = int (input("Ваше предложение: "))
tries = 1
if guess == the_number:
   print("Угадал")
else:
    print("Не угадал")
    
