import tkinter
import random
import json
from rabota_s_failami import *

filename = 'tasks.json'        
all_tasks = reader(filename)

def click0():
    task = {"Задача": entry0.get(), "Категория": entry1.get(), "Время": entry2.get()}
    all_tasks.append(task)

def click1():
    text_box.delete ('1.0',tkinter.END)
    s = ""
    for zadaniya in all_tasks:
            for i in zadaniya.keys():
                s += f"{i}: {zadaniya[i]}\n"
    text_box.insert('1.0',s) 
    
window = tkinter.Tk()

frameL = tkinter.Frame(window)
frameL.grid(row=0, column=0)

frameR = tkinter.Frame(window)
frameR.grid(row=0, column=1)

frame_tb = tkinter.Frame(window)
frame_tb.grid(row=0, column=2, rowspan =2)

frameButtons = tkinter.Frame(window)
frameButtons.grid(row=1, column=0, columnspan=2)


label0 = tkinter.Label (frameL, text = 'Задача')
label0.pack()

label1 = tkinter.Label(frameL, text = 'Категория')
label1.pack()

label2 = tkinter.Label(frameL, text = 'Время')
label2.pack()


entry0 = tkinter.Entry(frameR)
entry0.pack()

entry1 = tkinter.Entry(frameR)
entry1.pack()

entry2 = tkinter.Entry(frameR)
entry2.pack()

text_box = tkinter.Text(frame_tb, width = 50, height = 50)
text_box.pack()

button0 = tkinter.Button(frameButtons, text = 'Добавить задачу', command = click0)
button1 = tkinter.Button(frameButtons, text = 'Вывести список задач', command = click1)
button2 = tkinter.Button(frameButtons, text = 'Выход', command = window.destroy)
button0.pack()
button1.pack()
button2.pack()


window.mainloop()
writer(filename, all_tasks)


