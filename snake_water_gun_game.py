#Snake Water Gun Game
import random

def gameWin(comp,you):
    #If two values are equal, declare a tie!
    if comp == you:
        return None

    #Check all possibilities when computer choice 's'
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True

    #Check all possibilities when computer choice 'g'
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

    #Check all possibilities when computer choice 'w'
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True


print("Computer Turn: Snake(s) Water(w) or Gun(g)? ")
randNo= random.randint(1,3)

if randNo == 1:
    comp = 's'

elif randNo == 2:
    comp = 'w'

elif randNo == 3:
    comp = 'g'

you=input("Your Turns: Snake(s) Water(w) or Gun(g)? ")
a=gameWin(comp,you)

print(f"Computer choice:\n{comp}")
print(f"Your choice:\n{you}")

if a==None:
    print("The game is Tie!")

elif a:
    print("You Win!")

else:
    print("You Lose!")
