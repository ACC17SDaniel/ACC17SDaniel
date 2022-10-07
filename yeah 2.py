import plotly.express as px
file1 = open("onTime.txt", "r")
word = ""
wordList = []
letter = file1.read(1)
while letter != "":
    if letter == " " and word != "":
        wordList.append(word)
        word = ""
    elif letter == "\n" and word != "\n":
        wordList.append(word)
        word = ""
    elif letter == "," and word != ",":
        wordList.append(word)
        word = ""
    elif letter != " ":
        word = word+letter
    letter = file1.read(1)
for i in range(len(wordList)-2):
    if wordList[i] == "":
        wordList.pop(i)
for k in range(len(wordList)):
    wordList[k] = wordList[k].lower()
wordList.sort()
frqIndex = []
frqCount = []
frqIndex.append(wordList[0])
frqCount.append(1)
for j in range(1, len(wordList)):
    if wordList[j] == wordList[j-1]:
        frqCount[-1] = frqCount[-1]+1
    else:
        frqIndex.append(wordList[j])
        frqCount.append(1)
file2 = open("onTimeAnalysis.txt", "w")
for m in range(len(frqIndex)):
    file2.write(frqIndex[m]+" = "+str(frqCount[m])+"\n")
mode = 0
for n in range(1, len(frqIndex)):
    if frqCount[n] > frqCount[mode]:
        mode = n
file2.write("\n Mode = "+frqIndex[mode])
fig = px.bar(x = frqIndex, y = frqCount)
fig.show()
file2.close()