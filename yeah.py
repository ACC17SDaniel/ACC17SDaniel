def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num1 = int(input("gimme number"))
print("The factorial of", num1, "is", factorial(num1))

#

def fibonacci(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return (fibonacci(x-1)+fibonacci(x-2))
num1 = int(input("gimme number"))
for i in range(1, num1):
    print(fibonacci(i))

#

base = float(input("base"))
answer = float(input("answer"))
log = 0
if answer == 1:
    log = 0
elif answer > base:
    while answer >= base:
        answer = answer/base
        log +=1
    if answer != 1:
        print("nah")
    else:
        print(log)
else:
    print("nah")