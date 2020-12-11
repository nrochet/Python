import random

#Function to generate the numbers for euromillions (from 1 - 50)
def generateNumbers():
    result = []
    count = 5
    while count != 0:
        randomnumber = random.randint(1,50)

        if randomnumber not in result:
            result.append(randomnumber)
        count -= 1

    return result

#Function to generate the stars for euromillions (from 1 - 12)
def generateStars():
    result = []
    count = 2

    while count != 0:
        randomstar = random.randint(1,12)

        if randomstar not in result:
            result.append(randomstar)
        count -= 1

    return result


#Function to generate sets of numbers based on number of bets (each bet is a combo of 5 numbers and 2 stars)
def playGame(bets):
    bets = int(bets)
    while bets != 0:
        print("Numbers:", (generateNumbers()), "Stars:", (generateStars()))
        bets -= 1
    else: 
        return bets
print(playGame(23))