# импорт всех классов из библиотеки  Tk
from tkinter import *

from tkinter import messagebox

import model
import controller

# создание окна
window = Tk()

# положение окна
window.geometry('+600+350')

window.title("Игра в кости")

# вызывается контроллером, для передачи значения txt1 в контроллер
def chooseDiceNumber():
    return txt1.get()

# вызывается контроллером, для передачи значения txt2 в контроллер
def chooseBetAmount():
    return txt2.get()

# функц. reset() запускается событием кнопки btn3
def reset():
    txt1.delete(0,'end')
    txt2.delete(0,'end')

# вызывается контроллером
def showResult(message):
    lbl3['text'] = f'к-во очков : {message}'

# вызывается контроллером
def showDice(diceNumber):
    lbl4['text'] = f'кость : {diceNumber}'

# создание виджетов класса Label(отображение текстовой инф.)
lbl = Label(window, width=25, anchor="w",  text="Выберите кость")
lb2 = Label(window,width=25, anchor='w', text="Введите величину ставки")
lbl3 = Label(window, width=25,anchor='w', text = f'к-во очков : {model.getPoints()}')
lbl4 = Label(window, width=25, anchor='w', text='кость :')

# создание виджетов класса Entry(для ввода текстовой инф.)
txt1 = Entry(window,width=10)
txt2 = Entry(window,width=10)

# создание виджетов класса Button
btn = Button(window, width=10, text="кинуть кость", command=controller.launch)
btn3 = Button(window, width=15, text="сбросить", command=reset)

# разметка
lbl.grid(column=0, row=1)
lb2.grid(column=0, row=2)
lbl3.grid(column=0, row=4)
lbl4.grid(column=0, row=5)
txt1.grid(column=3, row=1)  
txt2.grid(column=3, row=2)
btn.grid(column=4, row=6)
btn3.grid(column=3, row=6)

def alarm():
    messagebox.showinfo('Ошибка', 'не корректные данные')

def andOfGames():
    messagebox.showinfo('','Конец игры')

# запуск окна
def getLoop():
    return window.mainloop