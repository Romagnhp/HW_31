from random import Random

def getPoints():
    return 500

# функиция throwDice() - генерации случайного числа от 1 до 6
def throwDice():
    return round(Random().random()*5)+1

# сравнение результатов
points = getPoints()
def calculatePoints(diceNumber, choosenDiceNumber, choosenBetAmount):

    global points

    if diceNumber == 6:
        points += 3
    else:
        points -= 1

    if diceNumber == choosenDiceNumber:
        points += (3*choosenBetAmount)
    else:
        points -= choosenBetAmount

    if points <= 0:
        points = False
    
    return points

