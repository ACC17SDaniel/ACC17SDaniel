file1 = open("i m.txt", "r")
numList = file1.read().split(",")
mean = 0
median = 0
mode = []
for m in range(len(numList)):
    numList[m] = int(numList[m])
numList.sort()
for i in range(len(numList)):
    mean += numList[i]
mean = (((mean/len(numList))*100)//1)/100
if len(numList)%2 == 0:
    median = ((((numList[len(numList)/2]+numList[(len(numList)/2)+1])/2)*100)//1)/100
else:
    median = (((numList[(len(numList)//2)+1])*100)//1)/100
freq = 1
highestFreq = 0
for j in range(len(numList)-1):
    if numList[j+1] == numList[j]:
        freq += 1
    else:
        if freq > highestFreq:
            mode = []
            highestFreq = freq
            mode.append(numList[j])
        elif freq == highestFreq:
            mode.append(numList[j])
        freq = 1
file2 = open("i dont even know anymore.txt", "w")
file2.write("Mean: "+str(mean)+"\nMedian: "+str(median)+"\n")
if len(mode) == 1:
    file2.write("Mode: "+str(mode[0]))
else:
    file2.write("Mode: "+str(mode[0]))
    for l in range(1, len(mode)):
        file2.write(" and "+str(mode[l]))
file2.close()   