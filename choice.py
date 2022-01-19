import random
import time
awesome = 1
while awesome == 1:
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
    whichSort = int(input("""i gave you a shuffled list tell me how you wanna sort it
1: bubl
2: not bubl"""))
    if whichSort == 1:
        i = 0
        j = 0
        storage = 0
        swap = 1
        checkCount = len(shuffledList)-1
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
    elif whichSort == 2:
        storage = 0
        select = 0
        i = 0
        j = 0
        swap = 1
        for k in range(1, len(shuffledList)):
            select = k
            swap = 1
            while select > 0:
                if swap == 1:
                    i = shuffledList[select]
                    j = shuffledList[select-1]
                    if i < j:
                        storage = i
                        i = j
                        j = storage
                        shuffledList[select] = i
                        shuffledList[select-1] = j
                        print(shuffledList)
                    else:
                        swap = 0
                    select = select-1
                else:
                    select = 0