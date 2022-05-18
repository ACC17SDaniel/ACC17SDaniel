file1 = open("78.txt", "r")
wordList = file1.read().split()
capitalCount = 0
wordCount = len(wordList)
numCount = 0
spaceCount = len(wordList)-1 #if you're not an idiot
word = ""
for i in range(len(wordList)):
    word = wordList[i]
    for j in range(len(word)):
        if (word[j]).isdigit() == True:
            numCount += 1
        elif (word[j]).isupper() == True:
            capitalCount += 1
file2 = open("1738 ay im like hey whats up hello.txt", "w")
file2.write("Capital Letters: "+str(capitalCount)+"\nSpaces: "+str(spaceCount)+"\nWords: "+str(wordCount)+"\nNumbers: "+str(numCount))#
file2.close()
        
            
        
