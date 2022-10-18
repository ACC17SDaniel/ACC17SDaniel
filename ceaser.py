alphabet = "abcdefghijklmnopqrstuvwxyz"
file = open("message.txt", "r")
file2 = open("message2.txt", "w")
message = file.read()
message = message.lower()
newmessage = ""
for i in range(len(message)):
    for j in range(len(alphabet)):
        if message[i] == " ":
            newmessage += " "
        elif message[i] == alphabet[j] and j != 25:
            newmessage += alphabet[j+1]
        elif message[i] == alphabet[j] and j == 25:
            newmessage += alphabet[0]
file2.write(newmessage)
file2.close()

file3 = open("message2.txt", "r")
file4 = open("message3.txt", "w")
shift = int(input("shift"))
message = file3.read()
newmessage = ""
for i in range(len(message)):
    for j in range(len(alphabet)):
        if message[i] == " ":
            newmessage += " "
        elif message[i] == alphabet[j] and j != 0:
            newmessage += alphabet[j-shift]
        elif message[i] == alphabet[j] and j == 0:
            newmessage += alphabet[25]
file4.write(newmessage)
file4.close()