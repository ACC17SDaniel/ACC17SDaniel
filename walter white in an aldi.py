file = open("unicode.txt", "r")
file2 = open("walt.txt", "w")
code = "j"
digit = ""
codeDigit = ""
binaryCode = ""
fullBinary = ""
utfCode = ""
while code != "":
    code = ""
    if digit == "":
        digit = file.read(1)
    code = code+digit
    digit = file.read(1)
    while digit != "U" and digit != "" :
        code = code+digit
        digit = file.read(1)
    code = code[4:]
    for i in range(len(code)):
        codeDigit = code[i]
        if codeDigit.isalpha() == True:
            if codeDigit == "a":
                codeDigit = "10"
            elif codeDigit == "b":
                codeDigit = "11"
            elif codeDigit == "c":
                codeDigit = "12"
            elif codeDigit == "d":
                codeDigit = "13"
            elif codeDigit == "e":
                codeDigit = "14"
            else:
                codeDigit = "15"
        codeDigit = int(codeDigit)
        while codeDigit != 0:
            binaryCode = binaryCode+str(codeDigit%2)
            codeDigit = codeDigit//2
        binaryCode = binaryCode[::-1]
        binaryCode = binaryCode.zfill(4)
        fullBinary = fullBinary+binaryCode
        binaryCode = ""
    if len(fullBinary) <= 7 or (len(fullBinary) == 8 and fullBinary[0] == "0"):
        utfCode = fullBinary.zfill(8)
    elif len(fullBinary) <= 11 or (len(fullBinary) == 12 and fullBinary[0] == "0"):
        if len(fullBinary) == 12:
            fullBinary = fullBinary[1:]
        fullBinary = fullBinary.zfill(11)
        utfCode = "110"+fullBinary[0:5]+" 10"+fullBinary[5:]
    elif len(fullBinary) <= 16:
        fullBinary = fullBinary.zfill(16)
        utfCode = "1110"+fullBinary[0:4]+" 10"+fullBinary[4:10]+" 10"+fullBinary[10:]
    elif len(fullBinary) <= 21:
        fullBinary = fullBinary.zfill(21)
        utfCode = "11110"+fullBinary[0:3]+" 10"+fullBinary[3:9]+" 10"+fullBinary[9:15]+" 10"+fullBinary[15:]
    file2.write(utfCode+"\n")
    fullBinary = ""
    
    
