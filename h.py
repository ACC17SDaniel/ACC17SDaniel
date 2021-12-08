def maxNumber():
    num1 = int(input("gimme number"))
    num2 = int(input("gimme number part 2"))
    if num1 > num2:
        print(str(num1)+"'s the bigger one")
    elif num2 > num1:
        print(str(num2)+"'s the bigger one")
    else:
        print("They're the same dumbass")
maxNumber()

def multiply():
    num1 = int(input("gimme number"))
    num2 = int(input("gimme number part 2"))
    print(str(num1)+" x "+str(num2)+" = "+str(num1*num2))
multiply()

def backwards():
    str = input("gimme string")
    awesome = ""
    for i in range(-1,(len(str)*-1)-1,-1):
        awesome = awesome+str[i]
    print(awesome)
backwards()

coolList = [1,2,3,4,5,6,7,8,9,10]
def evenList(awesomeList):
    for g in range(len(awesomeList)):
        if awesomeList[g]%2 == 0:
            print(awesomeList[g])
evenList(coolList)
        