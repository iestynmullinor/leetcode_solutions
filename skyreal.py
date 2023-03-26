#%%
print("dane")

# %%

def isValid(sub):
    containsDigit = any(map(str.isdigit, sub))
    containsCap = any(x.isupper() for x in sub)
    return ((containsDigit==False) and containsCap)

def getSubStrings(S):
    return [S[i:j] for i in range(len(S)) for j in range(i+1, len(S) + 1)]

def solution(S):
    subStrings = getSubStrings(S)
    validSubLengths = []

    for subString in subStrings:
        if isValid(subString):
            validSubLengths.append(subString)

    if (len(validSubLengths) == 0):
        return -1
    
    longest = max(validSubLengths, key=len)
    return len(longest)

    


# %%
