binaryList = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
hexList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
def BinToHex(j):
    for i in range(16):
        if j == binaryList[i]:
            return hexList[i]
file = open("walt.txt", "r")
code = "j"
hexCode = ""
while code != "":
    hexCode = ""
    code = file.readline()
    code = code[:-1]
    if len(code) != 0:
        if len(code) == 8:
            for k in range(2):
                hexCode = hexCode+BinToHex(code[4*k:4*(k+1)])
            print (chr(int(hexCode, 16)))
        elif len(code) == 17:
            code = code[3:8]+code[11:]
            code = code.zfill(12)
            for k in range(3):
                hexCode = hexCode+BinToHex(code[4*k:4*(k+1)])
            print (chr(int(hexCode, 16)))
        elif len(code) == 26:
            code = code[4:8]+code[11:17]+code[20:]
            for k in range(4):
                hexCode = hexCode+BinToHex(code[4*k:4*(k+1)])
            print (chr(int(hexCode, 16)))
        elif len(code) == 35:
            code = code[6:8]+code[11:17]+code[20:26]+code[29:]
            for k in range(5):
                hexCode = hexCode+BinToHex(code[4*k:4*(k+1)])
            print (chr(int(hexCode, 16)))
        print ("U+0x"+hexCode)