import random

running = True


## Starting with a while loop
while running:
    rolls = "a"
    sides = "a"
    total = 0

    while sides.isnumeric() == False:
        sides = input("How many sides does this die have? ")
        if sides.isnumeric() == False:
            print("You must enter a number.")
            continue
        
    sides = int(sides)
    if sides < 2:
        print("You much have a minimum of 2 sides")
        continue


    while rolls.isnumeric() == False:
        rolls = input("How many dice? ")
        if rolls.isnumeric() == False:
            print("You must enter a number.")
            continue
        if rolls < 1:
            print("You must roll at least 1 die.")
            continue
    rolls = int(rolls)


    for x in range(rolls):
        roll = random.randint(1,sides)
        total += roll
        print (x+1, ": ", roll)
    print("TOTAL: ", total)
    print("\n")

    rollAgain = input("Roll again (Y/N)? ")

    if rollAgain.upper() == "N":
        break
print("End Program")

