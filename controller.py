import model
import view_2 as view

def launch():

    points = model.getPoints()
    dice_Number = model.throwDice()
    choosen_DiceNumber = int(view.chooseDiceNumber())
    choosen_BetAmount = int(view.chooseBetAmount())

    value = model.calculatePoints(dice_Number, choosen_DiceNumber, choosen_BetAmount, points)
    print(value)

    view.showResult(value)
    view.showDice(dice_Number)

def main():
    view.getLoop()()

if __name__ == '__main__':
    main()     
