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
print("insert sort time :)")
time.sleep(1)
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
            
    