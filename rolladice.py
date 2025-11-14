#importing the random
import random

print(" Welcome to the Dice Rolling Simulator! 🎲 ")
# outer loop 
while True: 
    input("Press Enter to roll the dice...") #wait for the user to press enter
# inner loop
    while True:
        #generates a random integer from 1-6
        result = random.randint(1, 6)
# using match statement to print result
        match result:
            case 1:
                print("1️⃣ Just a one. Gotta start somewhere, right?")
            case 2:
                print("2️⃣ Hmm, two it is. Try again? ")
            case 3:
                print("3️⃣ Three's company! Right in the middle 🥉")
            case 4:
                print("4️⃣ Four! Things are heating up 🔥")
            case 5:
                print("5️⃣ Nice! You’re just one away from a six ")
            case 6:
                print("6️⃣ BOOM! A perfect six! ")
# rolls again automatically if result = 6
        if result == 6:
            print("🎉Since you hit a six, we're rolling again automatically...")
        else:
            break
# end of inner loop        
#asks the user if they want to roll again
    roll_again = input("Roll again? (y/n): ").strip().lower()
    if roll_again != 'y':
        print("Thanks for playing!")
        break
# exits the outer loop
