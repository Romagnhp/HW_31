# импорт всех классов из библиотеки  Tk
from tkinter import *

import controller

# окно
window = Tk()

window.geometry('+600+350')
window.title("Игра в кости")

def chooseDiceNumber():
    return txt1.get()

def chooseBetAmount():
    return txt2.get()

def chooseDiceNumber():
    return txt1.get()

def chooseBetAmount():
    return txt2.get()

def reset():
    txt1.delete(0,'end')
    txt2.delete(0,'end')

p = 0
def showResult(message):
    global p
    p = message
    lbl3['text'] = f'к-во очков : {p}'

def showDice(diceNumber):
    pass

lbl = Label(window, width=25, anchor="w",  text="Выберите кость")
lb2 = Label(window,width=25, anchor='w', text="Введите величину ставки")
lbl3 = Label(window, width=25,anchor='w', text = f'к-во очков : {p}')

txt1 = Entry(window,width=10)
txt2 = Entry(window,width=10)

btn = Button(window, width=10, text="кинуть кость", command=controller.launch)
btn3 = Button(window, width=15, text="сбросить", command=reset)

lbl.grid(column=0, row=1)
lb2.grid(column=0, row=2)
lbl3.grid(column=0, row=4)

txt1.grid(column=3, row=1)  
txt2.grid(column=3, row=2)

btn.grid(column=4, row=4)
btn3.grid(column=3, row=4)

def getLoop():
    return window.mainloop