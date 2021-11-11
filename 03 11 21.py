mainNumber = int(input("gimme a number stinky"))
numberStorage = mainNumber
digitCount = 0
while mainNumber != 0:
    mainNumber = mainNumber//10
    digitCount = digitCount+1
mainNumber = numberStorage
finalNumber = 0
digit = 0
while mainNumber != 0:
    digit = mainNumber%10
    digitCount = digitCount-1
    finalNumber = finalNumber+(digit*(10**digitCount))
    mainNumber = mainNumber//10
print(finalNumber)
    