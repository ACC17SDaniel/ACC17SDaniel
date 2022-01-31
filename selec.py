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
print("selection sort time :)")
time.sleep(1)
i = 0
j = 0
marker = 0
lowest = 0
while marker != len(shuffledList):
    i = shuffledList[marker]
    lowest = marker
    j = i
    for k in range(marker, len(shuffledList)):
        if shuffledList[k] < j:
            j = shuffledList[k]
            lowest = k
    shuffledList[marker] = j
    shuffledList[lowest] = i
    print(shuffledList)
    marker = marker+1
    