wordThing = str(input("gimme a word"))
wordThing = wordThing.lower()
palinCheck = 1
for check in range(0,(len(wordThing)//2)-1):
    if wordThing[check] == wordThing[-1(check)]:
        if palinCheck != 0:
            palinCheck = 2
    else:
        palinCheck = 0
if palinCheck != 0:
    print("yeah that's a palindrome right there")
else:
    print("sfjhsdgsghdgjgsgjkggsdsdgjhsdgsdgsdgsdgsdgsdgsdg")

        
