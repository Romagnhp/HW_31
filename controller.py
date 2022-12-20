import model
import view_2 as view

points = model.getPoints()

value = points

while not value == 0:

    dice_Number = model.throwDice()
    choosen_DiceNumber = int(view.chooseDiceNumber())
    choosen_BetAmount = int(view.chooseBetAmount())

    value = model.calculatePoints(dice_Number, choosen_DiceNumber, choosen_BetAmount, points)

    view.showResult(value)
    view.showDice(dice_Number)