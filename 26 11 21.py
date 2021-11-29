fileOpen = open("100Random.txt","r")
fileOpen2 = open("100Random.txt","r")
line = "h"
storage = ""
element = ""
numberList = []
while line != "":
    storage = fileOpen.readline(1)
    if storage.isdigit() == True:
        element = element+storage
    elif element != "":
        element = int(element)
        numberList.append(element)
        element = ""    
    line = fileOpen2.readline(1)
numberList.sort()
print(numberList[-1]-numberList[0])
fileOpen.close()
fileOpen2.close()
#
fileOpen = open("100Random.txt","r")
fileOpen2 = open("100Random.txt","r")
line = "h"
storage = ""
element = ""
numberList = []
while line != "":
    storage = fileOpen.readline(1)
    if storage.isdigit() == True:
        element = element+storage
    elif element != "":
        element = int(element)
        numberList.append(element)
        element = ""    
    line = fileOpen2.readline(1)
numberList.sort()
freqList = []
numberCheck = 1
freqCount = 0
for a in range(len(numberList)):
    if numberList[a] == numberCheck:
        freqCount = freqCount+1
    else:
        freqList.append(freqCount)
        freqCount = 0
        while numberList[a] != numberCheck:
            numberCheck = numberCheck+1
            if numberList[a] == numberCheck:
                freqCount = freqCount+1
            else:
                freqList.append(0)
print(freqList)
fileOpen.close()
fileOpen2.close()
#
fileOpen = open("100Random.txt","r")
fileOpen2 = open("100Random.txt","r")
line = "h"
storage = ""
number = ""
numberCount = 0
finalNumber = 0
while line != "":
    storage = fileOpen.readline(1)
    if storage.isdigit() == True:
        number = number+storage
    elif number != "":
        numberCount = numberCount+1
        number = int(number)
        finalNumber = finalNumber+number
        number = ""    
    line = fileOpen2.readline(1)
finalNumber = float(finalNumber)
finalNumber = finalNumber/numberCount
testNumber = finalNumber
while testNumber >= 1:
    testNumber = testNumber-1
if testNumber == 0:
    finalNumber = int(finalNumber)
print(finalNumber)
fileOpen.close()
fileOpen2.close()
#
fileOpen = open("100Random.txt","r")
fileOpen2 = open("100Random.txt","r")
line = "h"
storage = ""
element = ""
numberList = []
while line != "":
    storage = fileOpen.readline(1)
    if storage.isdigit() == True:
        element = element+storage
    elif element != "":
        element = float(element)
        numberList.append(element)
        element = ""    
    line = fileOpen2.readline(1)
numberList.sort()
median = 0
awesome = int(len(numberList)/2)
if len(numberList)%2 == 0:
    median  = numberList[awesome]
    median = median+numberList[awesome-1]
    median = median/2
    testNumber = median
while testNumber >= 1:
    testNumber = testNumber-1
if testNumber == 0:
    median = int(median)
    print(median)
fileOpen.close()
fileOpen2.close()
#
fileOpen = open("100Random.txt","r")
fileOpen2 = open("100Random.txt","r")
line = "h"
storage = ""
element = ""
numberList = []
while line != "":
    storage = fileOpen.readline(1)
    if storage.isdigit() == True:
        element = element+storage
    elif element != "":
        element = int(element)
        numberList.append(element)
        element = ""    
    line = fileOpen2.readline(1)
numberList.sort()
freqList = []
numberCheck = 1
freqCount = 0
for a in range(len(numberList)):
    if numberList[a] == numberCheck:
        freqCount = freqCount+1
    else:
        freqList.append(freqCount)
        freqCount = 0
        while numberList[a] != numberCheck:
            numberCheck = numberCheck+1
            if numberList[a] == numberCheck:
                freqCount = freqCount+1
            else:
                freqList.append(0)
mode = 0
modeFreq = 0
for b in range(len(freqList)):
    if freqList[b] > modeFreq:
        mode = b+1
        modeFreq = freqList[b]
print(mode)
    