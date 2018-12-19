# my_task.log
def reader(filename):
    import json
    try:
        with open(filename, 'r') as f_obj:
             vse_zada4i = json.load(f_obj)
        return vse_zada4i  
    except Exception as e:
        print (e)
        return []
        

def writer(filename, vse_zada4i):    
    import json    
    try:
        with open(filename, 'w') as f_obj:
            json.dump(vse_zada4i, f_obj)
    except Exception as e:
        print(e) 

filename = 'tasks.json'        
all_tasks = reader(filename)
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
        writer(filename, all_tasks)
        break
print(all_tasks)