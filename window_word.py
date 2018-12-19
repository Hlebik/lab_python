import tkinter
import random


def click():
    try:
        if entry.get() == word_ran[b]:
            label3.config (text = 'Вы угадали слово')
        else:
            label3.config (text = 'попробуй снова')
    except:
        label.config(text = 'Ошибка ввода')
        
word_ran = {'dog':'собака', 'cat':'кошка', 'bird':'птица', 'tiger': 'тигр', 'sea lion' : 'морской котик'} 
a = word_ran
lst = list(a)
b = random.choice(lst)
window = tkinter.Tk()

lable0 = tkinter.Label(text = 'Случайное слово:')
lable0.pack()
label = tkinter.Label(text = str(b))
label.pack()
label1 = tkinter.Label(text ='укажите перевод слова')
label1.pack()
label3 = tkinter.Label()
label3.pack()

frame = tkinter.Frame(window)
frame.pack()

entry = tkinter.Entry(frame)
entry.pack()

label2 = tkinter.Label(window)
label2.pack()
            
button1 = tkinter.Button(frame, text = 'Готово', command = click)
button2 = tkinter.Button(frame, text = 'Выход', command = window.destroy)
button1.pack()
button2.pack()

window.mainloop()

"""Программа отображает
случайное слово на английском
языке (из заранее созданного
словаря). Пользователь
пытается угадать слово на
русском языке."""
 






