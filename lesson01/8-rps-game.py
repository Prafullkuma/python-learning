
# value = input("Please enter a values ")
# print(value)
import sys
import random

print("")
playerchoice = input("Enter... \n 1.Rock \n 2.Paper \n 3.Scissors \n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1,2,or 3")

computerChoice = random.choice("123")

choice = int(computerChoice)

print("")

print("Your choose",player)
print("Python choose", choice)

if player == 1 and choice == 3:
    print("You win!")
elif player == 2 and choice == 1:
    print("You wins!")
elif  player == 3 and choice == 2:
    print("You wins!")
elif player == choice:
    print("Ties")
else: 
    print("Python wins")