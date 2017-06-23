from random import randrange

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and out run the natives.")

# Starting variables
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_traveled = -20
canteen_drinks = 3
oasis = randrange(21)

# Main program loop
done = False
while done == False:
    print("A. Drink from you canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night")
    print("E. Status check.")
    print("Q. Quit.")
    print("")
    user_choice = str(input("Please make your choice: "))

    # User wants to quit
    if user_choice.upper() == "Q":
        print("Thank you for playing")
        done = True

    # User wants a status check
    elif user_choice.upper() == "E":
        print("Miles traveled: ", miles_traveled)
        print("Drinks in canteen: ", canteen_drinks)
        print("The natives are", natives_traveled, "behind you")
        print("*******************")

    # User wants to stop for the night
    elif user_choice.upper() == "D":
        print("Your camel is happy to rest")
        camel_tiredness = 0
        natives_traveled += randrange(7, 15)

    # User wants to go ahead full speed
    elif user_choice.upper() == "C":
        miles_traveled += randrange(10, 21)
        camel_tiredness += randrange(1, 4)
        thirst += 1
        natives_traveled += randrange(7, 15)
        print(miles_traveled)

    # User wants to go ahead moderate speed
    elif user_choice.upper() == "B":
        miles_traveled += randrange(5, 13)
        thirst += 1
        camel_tiredness += 1
        natives_traveled += randrange(7, 15)
        print(miles_traveled)

    # User wants to drink from the canteen
    elif user_choice.upper() == "A":
        if canteen_drinks > 0:
            thirst = 0
            canteen_drinks -= 1
        else:
            print("You have no more water!")

    # User notification of user getting thirsty
    elif thirst > 4 and thirst < 6:
        print("You are thirsty")

    # User dies of thirst, game over
    elif thirst > 6:
        done = True
        print("You died of thirst!")

    if camel_tiredness in range(5, 9):
        print("Your camel is getting tired.")

    if camel_tiredness > 8:
        print("Your camel is dead.")
        print("GAME OVER")
        done = True

    elif miles_traveled == natives_traveled:
        print("The natives have caught you. GAME OVER")
        done = True

    if miles_traveled > 200:
        done = True
        print("You have escaped the desert. YOU WIN")

    # Random chance for oasis
    if oasis == miles_traveled:
        thirst = 0
        camel_tiredness = 0
        canteen_drinks = 3
        print("You have found an oasis! You have refilled your canteen and you camel is rested")


