#%%
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    found = False
    value = 1
    while (found==False):
        if (value in A):
            value +=1
        else:
            found = True
            return value

print(solution([1,2,4,5]))

# %%

def solution2(A):
    sortedA = sorted([x for x in A if x > 0])
    sortedAset = list(dict.fromkeys(sortedA))
    print(sortedAset)

    if (sortedAset==[]):
        return 1

    for i in range(len(sortedAset)):
        if ((i+1)!=sortedAset[i]):
            return i+1

    return(sortedAset[len(sortedAset)-1]+1)

print(solution2([1]))
    
# %%

import time
array = [x for x in range(10000)]
#array.remove(8325)
startTime1 = time.time()
sol1 = solution(array)
print(sol1)
time1 = time.time() - startTime1

startTime2 = time.time()
sol2 = solution2(array)
print(sol2)
time2 = time.time() - startTime2

print("time for solution 1: " + str(time1))
print("time for solution 2: " + str(time2))


# %%
