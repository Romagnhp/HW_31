import controller
import model

def getLoop():
    return mainloop

def chooseDiceNumber():
    return input('Выберите кость = ')

def chooseBetAmount():
    return input('Введите величину ставки = ')

def showResult(message):
    return print(f'К-во очков - {message}')

def showDice(diceNumber):
    print(f'Кость - {diceNumber}')

def alarm():
    print('Ошибка не корректные данные')

def andOfGames():
    print('Конец игры вы проиграли')

def mainloop():
    while model.points:
        controller.launch()
