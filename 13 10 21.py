#average thingy
import time
numberCount = 0
bigNumber = 0
while numberCount < 10:
    if numberCount == 0:
        coolNumber = int(input("gimme a number"))
    else:
        coolNumber = int(input("gimme another number"))
    bigNumber = bigNumber+coolNumber
    numberCount = numberCount+1
print("the average of those numbers is", bigNumber/10, ". pretty awesome")
#multiples of [REDACTED]
print("awesome multiplication table thing")
multiNumber = int(input("now what number have you forgotten how to multiply like the dumbass you are"))
multiCount = int(input("how many of those do you need"))
multiReal = 0
awesomeNumber = 0
while multiReal < multiCount:
    awesomeNumber = awesomeNumber+multiNumber
    print(multiNumber, "x", multiReal+1, "=", awesomeNumber)
    multiReal = multiReal+1
    time.sleep(0.05)
#hcf
hcfNumber1 = int(input("gimme a number"))
hcfNumber2 = int(input("gimme another number"))
if hcfNumber1 > hcfNumber2:
    hcfRemain = hcfNumber1%hcfNumber2
    hcfDivizor = hcfNumber2
    hcfExtra = hcfRemain
    while hcfRemain != 0:
        
#beeg number!
print("big number time")
bigTish = int(input("gimme a number to make big"))
bigCount = 1
bigMulti = bigTish
bigNumber = bigTish
if bigTish < 0:
    print("nah")
elif bigTish <= 1:
    print("the number is 1")
else:
    while bigCount < bigTish:
        bigMulti = bigMulti-1
        bigNumber = bigNumber*bigMulti
        bigCount = bigCount+1
    print("the number is", bigNumber)

#bin
deciNumber = int(input("i wanna convert a number to binary gimme one"))
binNumber = 0
digitNumber = 0
modNumber = 0
divideNumber = deciNumber
while divideNumber != 0:
    modNumber = divideNumber%2
    divideNumber = divideNumber//2
    binNumber = binNumber+(modNumber*(10**digitNumber))
    digitNumber = digitNumber+1
print(binNumber)
    
#run.
time.sleep(10)
ohNo = 0
while ohNo == 0:
    print("run.")
    time.sleep(0.25)
