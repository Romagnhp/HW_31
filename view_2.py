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

p = 0
def showResult(message):
    global p
    p = message
    lbl3['text'] = f'к-во {p}'

def showDice(diceNumber):
    pass

lbl = Label(window, width=25, anchor="w",  text="Выберите кость")
lb2 = Label(window,width=25, anchor='w', text="Введите величину ставки")
lbl3 = Label(window, width=25,anchor='w', text = f'к-во очков : {p}')

txt1 = Entry(window,width=10)
txt2 = Entry(window,width=10)

btn = Button(window, width=10, text="кинуть кость", command=controller.launch)
btn1 = Button(window, width=10, text="ввод", command=chooseDiceNumber)
btn2 = Button(window, width=10, text="ввод", command=chooseBetAmount)
btn3 = Button(window, width=15, text="сделать ставку", command='click')

lbl.grid(column=0, row=1)
lb2.grid(column=0, row=2)
lbl3.grid(column=0, row=4)

txt1.grid(column=3, row=1)  
txt2.grid(column=3, row=2)

btn.grid(column=4, row=4)
btn1.grid(column=4, row=1)
btn2.grid(column=4, row=2)
btn3.grid(column=3, row=4)

def getLoop():
    return window.mainloop