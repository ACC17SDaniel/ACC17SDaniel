fileName = input("gimme the name of the filly goofy ahh")
file = open(fileName, "r")
done = False
line = ""
lineCount = 0
charCount = 0
wordCount = 0

while done == False:
    line = file.readline()
    if line == "":
        done = True
    else:
        lineCount = lineCount+1
        line = line[0:-1]
        if len(line) != 0:
            for j in range(len(line)):
                if line[j] == " ":
                    if j != 0:
                        wordCount = wordCount+1
                else:
                    charCount = charCount+1
            wordCount = wordCount+1
print("Lines: "+str(lineCount)+"\nWords: "+str(wordCount)+"\nCharacters: "+str(charCount))            
                    
            