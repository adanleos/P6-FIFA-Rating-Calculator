import math
import numpy as np
from itertools import combinations_with_replacement

#Function for calculating the overall rating        
def ratingCalc(ratings):
    totalExcess = 0
    ratingSum = sum(ratings)
    avgRating = ratingSum / 11
    for f in range(11):
        if ratings[f] > avgRating:
            totalExcess = totalExcess + ratings[f] - avgRating
    calculatedRating = math.floor(round(ratingSum + totalExcess) / 11)
    return calculatedRating

maxRating = 99
minRating = 47
maxPlayers = 11

#Get list of ratings and make sure data is valid
while True:
    try:
        playerRatingsInput = input("Enter the ratings (47-99) of the players you have, separated by a space. (1 Min, 11 Max) ")
        inputPlayerRatings = list(map(int, playerRatingsInput.split()))
        ratingsRes = all(ele <= maxRating and ele >= minRating for ele in inputPlayerRatings) 
        if ratingsRes == False:
            print("Error: Enter ratings between 47 and 99.")
            continue
        elif len(inputPlayerRatings) >= maxPlayers:
            print("Error: You entered more players than are allowed on the pitch.")
            continue
        elif len(inputPlayerRatings) <= 0:
            print("Error: You need to enter at least one player.")
            continue
        else:
            break
    except:
        print("Error: Enter valid ratings.")
        continue
#Get desired rating and make sure it is valid rating        
while True:
    try:
        desiredRating = int(input("Enter the desired squad rating: "))
        if desiredRating < 1 or desiredRating > 99:
            print("Error: Enter an integer between 47 and 99.")
            continue
        else:
            break
    except:
        print("Error: Enter an integer between 47 and 99.")
        continue
#Get range of player ratings to try for combination
while True:
    try:
        ratingsRangeInput = input("Enter the range of ratings you would like to try, separated by a space. (Ex. '82 85') ")
        ratingsRange = list(map(int, ratingsRangeInput.split()))
        rangeRes = all(ele <= maxRating and ele >= minRating for ele in ratingsRange)
        if rangeRes == False:
            print("Error: Enter ratings between 47 and 99.")
            continue
        elif ratingsRange[0] >= ratingsRange[1]:
            print("Error: Make sure the first number is smaller than the second.")
            continue
        elif len(ratingsRange) > 2:
            print("Error: Enter only two integers.")
            continue
        elif len(ratingsRange) <= 1:
            print("Error: You need to enter two integers.")
            continue
        else:
            break
    except:
        print("Error: Enter valid ratings.")
        continue
        
numRemainingPlayers = maxPlayers - len(inputPlayerRatings)
calcArray = inputPlayerRatings.copy()
ratingsRangeList = range(ratingsRange[0],ratingsRange[1]+1)

array = list(combinations_with_replacement(ratingsRangeList ,numRemainingPlayers))

for i in range(len(array)):
        calcArray = inputPlayerRatings + list(array[i])
        finalCalcRating = ratingCalc(calcArray)
        if finalCalcRating = desiredRating:
            print("The squad "+ str(calcArray) +" has an overall rating of " + str(finalCalcRating) +".")