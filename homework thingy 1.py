print("oh hello wanna do some funny things with code for a quick sec")
firstNumber = int(input("ok what's your first number"))
secondNumber = int(input("gimme the second one now"))
if firstNumber > secondNumber:
    print(firstNumber, "is bigger than", secondNumber, "ha")

elif firstNumber < secondNumber:
    print(secondNumber, "is bigger than", firstNumber, "ha")
    
else:
    print("you picked the same number twice, how original")
    
myAge = int(input("ok now gimme your age i wanna see if you can vote or not"))
if myAge >= 18:
    print("you can vote now don't be stupid about it")
    
else:
    print("go beat clubstep then come back")

coolNumber = int(input("ok gimme another number"))
if coolNumber%2 == 1:
    print("that's an odd number right there buckaroo")

else:
    print("even")

if coolNumber%7 == 0:
    print ("oh yeah you picked a number that's divisible by 7 that's pretty awesome")

else:
    print("stinky")
    
if coolNumber%5 == 0:
    print ("hello there")

else:
    print("ew bye")
    
elecCharge = int(input("oh yeah how many units of electricity have you used recently"))

if elecCharge < 100:
    print ("you are free")
    
elif elecCharge < 200:
    print ("you now cost", (elecCharge-100)*5, "cent")

else:
    print ("you now cost", ((elecCharge-200)*10)+500, "cent")
    
print("oh yeah btw the last digit of your awesome number was", coolNumber%10)
if (coolNumber%10)%3 == 0:
    print ("it's also divisible by 3 awesome")

else:
    print("what is your problem man")

weekNumber = int(input("gimme a number from 1 to 7"))
if weekNumber == 1:
    print("moday")

elif weekNumber == 2:
    print("tuday")
    
elif weekNumber == 3:
    print("weday")
    
elif weekNumber == 4:
    print("thuday")
    
elif weekNumber == 5:
    print("fiday")
    
elif weekNumber == 6:
    print("sarday")
    
elif weekNumber == 7:
    print("suday")
    
else:
    print("no")

celTemp = float(input("gimme a temperature in celcius (the only good measuring system)"))
farTemp = 1.8*celTemp+32
farTemp = str(round(farTemp, 2))
print("that's", farTemp, "in the stupid measuring system")
print ("ok we got a lot here so here we go")
monDay = int(input("what day of the month is it"))
yrMonth = int(input("what month is it (as a number please)"))
if yrMonth == 1:
    yrMonth == 13

if yrMonth == 2:
    yrMonth == 14
    
awesomeYear = int(input("what year is it"))
yearOne = awesomeYear//100
yearTwo = awesomeYear%100

weekNumber = (monDay+((13*(yrMonth+1))/5)+yearTwo+(yearTwo/4)+(yearOne/4)-(2*yearOne))

if weekNumber == 1:
    print("moday")

elif weekNumber == 2:
    print("tuday")
    
elif weekNumber == 3:
    print("weday")
    
elif weekNumber == 4:
    print("thuday")
    
elif weekNumber == 5:
    print("fiday")
    
elif weekNumber == 6:
    print("sarday")
    
elif weekNumber == 7:
    print("suday")