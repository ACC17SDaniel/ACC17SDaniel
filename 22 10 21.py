creditCardNumber = int(input("give credit card number"))
storage1 = creditCardNumber
digitLength = 0
while creditCardNumber != 0:
    creditCardNumber = creditCardNumber//10
    digitLength = digitLength+1
creditCardNumber = storage1
if digitLength > 16:
    print ("fake")
elif digitLength < 13:
    print("fake")
else:
    theStankyLeg = 0
    while theStankyLeg != digitLength-2:
        creditCardNumber = creditCardNumber//10
        theStankyLeg = theStankyLeg+1
    if creditCardNumber != 37:
        if creditCardNumber//10 != 4:
            print("fake")
        elif creditCardNumber//10 != 5:
            print("fake")
        elif creditCardNumber//10 != 6:
            print("fake")
        else:
            creditCardNumber = storage1
            oddDigits = 0
            evenDigits = 0
            while creditCardNumber != 0:
                oddDigits = oddDigits+(creditCardNumber%10)
                creditCardNumber = creditCardNumber//10
                weirdDigit = 2*(creditCardNumber%10)
                if weirdDigit//10 > 0:
                    finalDigit = (weirdDigit%10)+(weirdDigit//10)
                else:
                    finalDigit = weirdDigit
                evenDigits = evenDigits+finalDigit
                creditCardNumber = creditCardNumber//10
            realNumber = oddDigits+evenDigits
            if realNumber%10 == 0:
                print("real")
            else:
                print("fake")
    else:
        creditCardNumber = storage1
        oddDigits = 0
        evenDigits = 0
        while creditCardNumber != 0:
            oddDigits = oddDigits+(creditCardNumber%10)
            creditCardNumber = creditCardNumber//10
            weirdDigit = 2*(creditCardNumber%10)
            if weirdDigit//10 > 0:
                finalDigit = (weirdDigit%10)+(weirdDigit//10)
            else:
                finalDigit = weirdDigit
            evenDigits = evenDigits+finalDigit
            creditCardNumber = creditCardNumber//10
        realNumber = oddDigits+evenDigits
        if realNumber%10 == 0:
            print("real")
        else:
            print("fake")
                
    