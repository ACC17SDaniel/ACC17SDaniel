print("""Python
programming
is
great
fun! :)""")
#
bigString = str(input("literally just keysmash lol"))
finalNumber = 0
for cHeco in range(0,len(bigString)):
    digitCheck = bigString[cHeco]
    check = digitCheck.isdigit()
    if check == True:
        digitCheck = int(digitCheck)
        finalNumber = finalNumber+digitCheck
print(finalNumber)
#
sentence = str(input("sentence now"))
print(sentence.replace(" ","-"))
#
vowelString = str(input("i will take your vowels"))
vowelLength = 0
vowelString = vowelString.lower()
while vowelLength != len(vowelString):
    ch = vowelString[vowelLength]
    if ch =="a" or ch=="e" or ch == "i" or ch == "o" or ch == "u":
        print(ch)
    vowelLength = vowelLength+1
#
vowelString = str(input("i will take your c"))
vowelLength = 0
vowelString = vowelString.lower()
constoCount = 0
while vowelLength != len(vowelString):
    ch = vowelString[vowelLength]
    if ch =="a" or ch=="e" or ch == "i" or ch == "o" or ch == "u":
        funny = 1
    else:
        constoCount = constoCount+1
    vowelLength = vowelLength+1
print(constoCount)
#
sentence = str(input("sentence now"))
print(sentence.replace("-","""
"""))