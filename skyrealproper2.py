#%%
print("dane")
# %%

#returns the sum of digits in an integer
def addDigits(num):
    stringVal = str(num)
    intArray = map(int, stringVal.strip())
    return sum(intArray)

#given a list of numbers, finds the largest value that is the sum of two of these numbers
def findMaxFromGroup(vals):
    largest = max(vals)
    vals.remove(largest)
    secondLargest = max(vals)
    return largest+secondLargest


def solution(S):
    
    valSumDict = {}

    #creates dictionary of groups of numbers with same digitSum and their values
    for s in S:
        sumOfDigits = addDigits(s)
        if sumOfDigits in valSumDict:
            valSumDict[sumOfDigits].append(s)
        else:
            valSumDict.update({sumOfDigits : [s]})

    
    maxValue = -1
    #for each group of numbers, finds the largest 2 digit sum
    for listOfNos in valSumDict.values():
        if len(listOfNos) >=2:
            biggestSum = findMaxFromGroup(listOfNos)
            if biggestSum > maxValue:
                maxValue = biggestSum
            
    return maxValue




# %%
