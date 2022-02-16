#Program 1
l = int(input("enter the lower value"))
u = int(input("enter the upper value"))
m = int(input("enter the measurement"))
verdict = False
if m >= l and m <= u:
    verdict = True
print(verdict)

#Program 2
primeList = []
k = int(input("input k"))
def primeFinder(a):
    check = True
    for b in range(2, a//2+1):
        if a%b == 0:
            check = False
    return check
number = 1
verdict = False
while len(primeList) != k:
    number = number+1
    verdict = primeFinder(number)
    if verdict == True:
        primeList.append(number)
notPrime = primeList[-1]
verdict = True
primeCheck = True
while primeCheck == True:
    notPrime = notPrime+1
    verdict = True
    for i in range(len(primeList)):
        if notPrime%primeList[i] == 0:
            verdict = False
    if verdict == True:
        primeCheck = primeFinder(notPrime)
print(notPrime)

#Program 3
k = int(input("how many different weights are there"))
differentWeights = []
for j in range(k):
    element = int(input("gimme a weight"))
    differentWeights.append(element)
weight = int(input("what's the weight of the present"))
differentWeights.sort()
finalAnswer = []
highestThing = k-1
while highestThing != 0:
    while (weight >= differentWeights[highestThing]):
        weight = weight-differentWeights[highestThing]
        finalAnswer.append(differentWeights[highestThing])
    highestThing = highestThing-1
if len(finalAnswer) != 0:
    print("Tara can weigh the present using", len(finalAnswer), "weights")
else:
    print("MINUS ONE")
print("\n")