import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters

    a = int(input("The probability that play A wins on a serve:"))
    b = int(input("The probability that play B wins on a serve:"))
    n = int(input("How many simulations:"))

    return a,b,n

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    #   abilities are represented by the probability of winning a serve
    # Returns number of wins for A and B

    winsA = 0
    winsB = 0


    for x in range(0,n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1

    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates n games of racquetball between players whose
    #   abilities are represented by the probability of winning a serve
    # Returns number of wins for A and B

    serving = "A"
    scoreA = 0
    scoreB = 0

    while gameOver(scoreA, scoreB) != True:
        if serving == "A":
            Test = random.randint(0, 100)
            if Test < probA:
                scoreA += 1
            else:
                serving = "B"
                
        if serving == "B":
            Test2 = random.randint(0, 100)
            if Test2 < probB:
                scoreB += 1
            else:
                serving = "A"
            
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for racquetball game
    # Returns True if either player scores 15 points, False otherwise

    if a > 15 or b > 15:
        return True
    else:
        return False
    
   

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == "__main__":
    main()



    
            
