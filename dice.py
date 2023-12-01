import random

print("How many dice would you like to roll?")

### Validate Input
while True:
    try:
        numberPicked = int(input("Type how many d20's you'd like to roll (between 1 and 5): "))
        if(numberPicked > 0 and numberPicked < 6):
            break
        else:
            print("Invalid input. Try again.")
    except:
        print("Please provide a number.")

def rollDice(amountOfDice):
            possibleFaces = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            for die in range(amountOfDice):
                roll = random.choice(possibleFaces)
                print("Die ", die + 1, ": ", roll)

rollDice(numberPicked)