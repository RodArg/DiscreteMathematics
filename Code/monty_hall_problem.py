"""
Author: Rodrigo Arguello
"""
import random

def runTrials():
    success = 0
    #for loop is to run 100 trials with random selection of each door
    for i in range(0,100):
        prize = random.randint(1,3)
        guess = random.randint(1,3)
        guess2 = random.randint(1,3);
        reveal = random.randint(1,3)
        #ensures the revealed goat is not the guess and is not the car (aka the prize)
        while(reveal == guess or reveal == prize):
            reveal = random.randint(1,3)
        #ensures that the second guess is the item that was not first guess and not the revealed goat
        while(guess2 == reveal or guess2 == guess):
            guess2 = random.randint(1,3)
        #if the second guess was the car, mark that as a success
        if(guess2 == prize):
            success += 1
    return success

def printTrials(n, yesNo):
    avg = 0
    if(yesNo == "Y"):
        print("Each 100 trials averaged: ")
    #adds up n amount of success rates
    for i in range(1,n+1):
        show = runTrials()
        avg += show
        #print each success rate
        if (yesNo == "Y"):
            print("(",i,")" ,show,sep='')
    #avg = average amount of success rates (total success rate percentage over # of success rates)
    avg /= n
    print("The average of all trials is:",avg)
    
print("We'll show through simulation that changing the selection in the Monty Hall problem leads to a 66% success rate.")
n = int(input("Input the number of 100 attempts you'd like to carry out: "))
yesNo = input("Would you like to show the average for each 100 trials? (Y/N) ")
print(printTrials(n,yesNo))
