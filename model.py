from random import Random

def getPoints():
    return 500

# функиция throwDice() - генерации случайного числа от 1 до 6
def throwDice():
    return round(Random().random()*5)+1

# сравнение результатов
def calculatePoints(diceNumber, choosenDiceNumber, choosenBetAmount, points):

    temp = points

    if diceNumber == 6:
        temp = points + 3
    else:
        temp = temp - 1

    if diceNumber == choosenDiceNumber:
        temp = temp + (3*choosenBetAmount)
    else:
        temp = temp - choosenBetAmount
    
    return temp

