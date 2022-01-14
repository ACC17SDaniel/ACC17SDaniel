import random
import time
shuffledList = []
element = 0
duplCheck = 1
while len(shuffledList) < 8:
    duplCheck = 1
    element = random.randint(1, 8)
    for h in range(len(shuffledList)):
        if element == shuffledList[h]:
            duplCheck = 0
    if duplCheck == 1:
        shuffledList.append(element)
print(shuffledList)
print("bubble sort time :)")
time.sleep(1)
log = open("bubl log.txt", "w")
i = 0
j = 0
storage = 0
swap = 1
descending = True
passCount = 0
checkCount = len(shuffledList)-1
if descending == False:
    while checkCount != 0:
        while swap == 1:
            swap = 0
            passCount = passCount+1
            log.write("BEFORE PASS "+str(passCount)+": "+str(shuffledList)+"\n")
            log.write("PASS "+str(passCount)+"\n")
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
                    log.write(str(shuffledList)+" Comparing L["+str(k)+"] and L["+str(k+1)+"] Swap: "+str(j)+" and "+str(i)+"\n")
                    print(shuffledList)
                else:
                   log.write(str(shuffledList)+" Comparing L["+str(k)+"] and L["+str(k+1)+"] No Swap\n") 
            checkCount = checkCount-1
else:
    while checkCount != 0:
        while swap == 1:
            swap = 0
            passCount = passCount+1
            log.write("BEFORE PASS "+str(passCount)+": "+str(shuffledList)+"\n")
            log.write("PASS "+str(passCount)+"\n")
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
                    log.write(str(shuffledList)+" Comparing L["+str(k)+"] and L["+str(k+1)+"] Swap: "+str(j)+" and "+str(i)+"\n")
                    print(shuffledList)
                else:
                   log.write(str(shuffledList)+" Comparing L["+str(k)+"] and L["+str(k+1)+"] No Swap\n") 
            checkCount = checkCount-1
log.write("OUTPUT(sorted list): "+str(shuffledList)+"\n")
log.close()
    