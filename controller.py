import model
import view_2 as view

def check(value1, value2):
    if value1 in [1,2,3,4,5,6] and value2 > 0:
        return True
    else:
        False

def launch():

    choosen_DiceNumber = view.chooseDiceNumber() 
    choosen_BetAmount = view.chooseBetAmount()

    if choosen_DiceNumber.isnumeric() and choosen_BetAmount.isdigit():
        choosen_DiceNumber = int(choosen_DiceNumber)
        choosen_BetAmount = int(choosen_BetAmount)
    else:
        view.alarm()

    if check(choosen_DiceNumber, choosen_BetAmount):
        
    
        dice_Number = model.throwDice()
        value = model.calculatePoints(dice_Number, choosen_DiceNumber, choosen_BetAmount)
       

        view.showResult(value)
        view.showDice(dice_Number)

    else:
        view.alarm()


def main():
    view.getLoop()()
    
if __name__ == '__main__':
    main()     

