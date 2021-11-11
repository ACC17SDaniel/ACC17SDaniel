#for loops
import time
print("hello have some numbers")
time.sleep(1)
for smolNumbers in range(1,11):
    print(smolNumbers)
    time.sleep(0.25)
for power in range(2,4):
    time.sleep(1)
    for smolNumbers in range(1,11):
        print(smolNumbers**power)
        time.sleep(0.25)
time.sleep(1)
#
evenSum = 0
for someNumbers in range(10,21,2):
    evenSum = evenSum+someNumbers
print(evenSum)
time.sleep(1)
#
for evenNumbers in range(20,1,-2):
    print(evenNumbers)
    time.sleep(0.25)
time.sleep(1)
#
starCount = int(input("hello gimme a number cool person"))
for a in range(1,starCount+2):
    for b in range(1,a):
        print("*", end ="")
    print()