#%%
print("dane")
# %%

#returns true if a valid move can be made
def checkForMove(aCount,bCount,nCount):
    if ((aCount >= 3) and (bCount >=1) and (nCount >= 2)):
        return True
    else:
        return False

def solution(S):
    # Implement your solution here
    aCount = 0
    bCount = 0
    nCount = 0

    #finds nymber of As,Bs,Ns in string
    for s in S:
        if s == "A":
            aCount+=1
        elif s == "B":
            bCount+=1
        elif s == "N":
            nCount+=1
    
    if (checkForMove(aCount, bCount, nCount)==False):
        return 0

    else:
        noOfMoves = 0
        while (checkForMove(aCount,bCount,nCount)):
            noOfMoves+=1
            aCount-=3
            bCount-=1
            nCount-=2
    
    return noOfMoves
    
solution("HUGYSIAG")

    

# %%

def solution2(S):

    #filteredS = [x for x in S if (x=="A" or x=="B" or x=="N")]

    aCount = 0
    bCount = 0
    nCount = 0

    #finds nymber of As,Bs,Ns in string
    for s in S:
        if s == "A":
            aCount+=1
        elif s == "B":
            bCount+=1
        elif s == "N":
            nCount+=1

    maxA = aCount//3
    maxB = bCount
    maxN = nCount//2

    return min([maxA,maxB,maxN])

solution2("BANANA")
# %%

import time
string = ("BANANANANANAHVJKASVKCJALSVI" *3703 ) + "B"
startTime1 = time.time()
sol1 = solution(string)
print(sol1)
time1 = time.time() - startTime1

startTime2 = time.time()
sol2 = solution2(string)
print(sol2)
time2 = time.time() - startTime2

print("time for solution 1: " + str(time1))
print("time for solution 2: " + str(time2))

# %%
