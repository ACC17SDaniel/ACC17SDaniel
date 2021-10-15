addNumber = int(input("gimme a number with multiple digits maybe"))
if addNumber < 10:
    print("you absolute buffoon what did i just say")
else:
    storageNumber = 0
    finalNumber = 0
    while addNumber != 0:
        storageNumber = addNumber%10
        addNumber = addNumber//10
        finalNumber = finalNumber+storageNumber
    print("i just added the digits for you the answer is", finalNumber)
#
print("oh yeah btw here's some armstrong numbers")
checkNumber = 100
storageNumber = 0
finalNumber = 0
checkStorage = 0
while checkNumber <= 500:
    finalNumber = 0
    checkStorage = checkNumber
    while checkNumber != 0:
        storageNumber = checkNumber%10
        checkNumber = checkNumber//10
        finalNumber = (finalNumber+storageNumber**3)
    if finalNumber == checkStorage:
        print(checkStorage)
    checkNumber = checkStorage
    checkNumber = checkNumber+1
#


#
onlyPositive = int(input("gimme a positive number"))
while onlyPositive < 0:
    print("no")
    onlyPositive = int(input("gimme a positive number"))
print("awesome")