# import tkinter

# gui = tkinter.Tk()
# gui.mainloop()

# def chooseDiceNumber():
#     return 0

# def chooseBetAmount():
#     return 0

# def showResult(message):
#     pass

# def showDice(diceNumber):
#     pass

from tkinter import *

window = Tk()

window.title("Игра в кости")

lbl = Label(window, text="Выберите кость для ставки")
lb2 = Label(window, text="Введите величину ставки")

btn1 = Button(window, width=10, text="ввод", command='clicked')
btn2 = Button(window, width=10, text="ввод", command='clicked')
btn = Button(window, width=10, text="Отправить", command='clicked')

txt1 = Entry(window,width=10)
txt2 = Entry(window,width=10)

lbl.grid(column=0, row=1)
lb2.grid(column=0, row=2)

txt1.grid(column=3, row=1)
txt2.grid(column=3, row=2)

btn1.grid(column=4, row=1)
btn2.grid(column=4, row=2)
btn.grid(column=4, row=4)

window.mainloop()


def chooseDiceNumber():
    return txt1.get()

def chooseBetAmount():
    return txt2.get()

def showResult(message):
    pass

def showDice(diceNumber):
    pass