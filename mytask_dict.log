# my_task.log

all_tasks = []
while True:
    print("""Просто todo:
        1. Добавить задачу.
        2. Вывести список задач.
        3. Выход.""")

    num = int(input("Укажите число: "))
    if num == 1:
        task = input("Сформулируйте задачу:")
        kat = input("Добавьте категорию к задаче:")
        time = input("Добавьте время к задаче:")

        task_1 = [task, kat, time]
        all_tasks.append(task_1)
    elif num == 2:
        for i in all_tasks:
            #print("Задача:", i[0], "Категория:", i[1], "Дата:", i[2])
            print(f"Задача: {i[0]} Категория: {i[1]} Дата: {i[2]}")
    elif num == 3:
        print("Выход.")
        break
