# first we want to generate random number and the ask user to guess the numbe and if the guessed number is less than target then we say to use is "your number is small" and also same for bigger number

import random


target = random.randint(1,100)

while True:
    userChoice = input("Guess the target or Quit(Q) :")

    if(userChoice == "Q"):
        break


    userChoice = int(userChoice)

    if(userChoice == target):
        print("Sucess : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Uour number was too small. Take bigger guess...")
    else:
        print("Your number is too big. Take a smaller guess...")     

print("----------GAME OVER------------")