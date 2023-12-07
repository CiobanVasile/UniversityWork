def greedy(c):
    """
       Greedy algorithm
       c - a list of candidates
       return a list (B) the solution found (if exists) using the greedy strategy, None if the algorithm
       selectMostPromissing - a function that return the most promising candidate
       acceptable - a function that returns True if a candidate solution can be extended to a solution
       solution - verify if a given candidate is a solution
    """
    b = [] #start with an empty set as a candidate solution
    while not solution(b) and c!=[]:
        #select the local optimum (the best candidate)
        candidate = selectMostPromissing(c)
        #remove the current candidate
        c.remove(candidate)
        #if the new extended  candidate solution is acceptable
        if acceptable(b+[candidate]):
            b.append(candidate)

    if solution(b):
        return b
    #there is no solution
    return None


#Let us consider that we have a sum M of money and coins of 1, 5, 25 units (an unlimited number of coins).
#The problem is to establish a modality to pay the sum M using a minimum number of coins.

def selectMostPromissing(c):
    """
      select the largest coin from the remaining coins
      candidate coins
      return a coin
    """
    return max(c)

def solution(b):
    """
      verify if a candidate solution is an actual solution
      basically verify if the coins conduct to a sum
    """
    sum = _computeSum(b)
    return sum==SUM

def acceptable(b):
    sum = _computeSum(b)
    return sum<=SUM

def _computeSum(b):
    sum = 0
    for coin in b:
        nrCoins = (SUM-sum) // coin
        #if this is in a candidate solution we need to use at least 1 coin
        if nrCoins==0: nrCoins =1
        sum += nrCoins*coin
    return sum

def printSol(b):
#    print b
    solStr = ""
    sum = 0
    for coin in b:
        nrCoins = (SUM-sum) // coin
        solStr+=str(nrCoins)+"*"+str(coin)
        sum += nrCoins*coin
        if SUM-sum>0:solStr+=" + "
    print (solStr)


COINS = [1, 5, 25]
SUM=43

#the solution is not optimal  - optimal = 1*25+3*5
# COINS = [1, 5, 12, 25]
# SUM=40

#the solution is not optimal  - optimal = 3*12
# COINS = [1, 5, 12, 25]
# SUM=36

rez = greedy(COINS)
printSol(rez)
