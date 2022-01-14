import random
import time
shuffledList = []
element = 0
duplCheck = 1
while len(shuffledList) < 32:
    duplCheck = 1
    element = random.randint(1, 32)
    for h in range(len(shuffledList)):
        if element == shuffledList[h]:
            duplCheck = 0
    if duplCheck == 1:
        shuffledList.append(element)
print(shuffledList)
print("bubble sort time :)")
time.sleep(1)
i = 0
j = 0
storage = 0
swap = 1
descending = True
checkCount = len(shuffledList)-1
if descending == False:
    while swap == 1:
        swap = 0
        while checkCount != 0:
            for k in range(checkCount):
                i = shuffledList[k]
                j = shuffledList[k+1]
                if i > j:
                    storage = i
                    i = j
                    j = storage
                    shuffledList[k] = i
                    shuffledList[k+1] = j
                    swap = 1
                    print(shuffledList)
            checkCount = checkCount-1
else:
    while swap == 1:
        swap = 0
        while checkCount != 0:
            for k in range(checkCount):
                i = shuffledList[k]
                j = shuffledList[k+1]
                if i < j:
                    storage = i
                    i = j
                    j = storage
                    shuffledList[k] = i
                    shuffledList[k+1] = j
                    swap = 1
                    print(shuffledList)
            checkCount = checkCount-1

    