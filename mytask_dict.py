all_tasks = []
while True:
    print("""Просто todo:
        1. Добавить задачу.
        2. Вывести список задач.
        3. Выход.""")
    num = int(input("Укажите число: "))
    if num == 1:
        text = input("Сформулируйте задачу:")
        kat = input("Добавьте категорию к задаче:")
        time = input("Добавьте время к задаче:")
        task = {"Задача": text, "Категория": kat, "Время": time}
        all_tasks.append(task)
    elif num == 2:
        for zadaniya in all_tasks:
            for i in zadaniya.keys():
                print(f"{i}: {zadaniya[i]}")
    elif num == 3:
        print("Выход.")
        break 

