#RPG
#Inputs: Gamemode, Character Selection, Attacks
#Hypotheses 1: Random characters, One charges a large amount of times and attacks, other randomly attacks: Prediction: Charging character loses
#Hypotheses 2: Random characters, One switches between attacking and defending every turn, other randomly attacks: Prediction: Pattern character wins
import random
import time
import csv
csvFile = open("funny.csv", "w")
writer = csv.writer(csvFile)

print("In a world where nothing makes any sense whatsoever...")
time.sleep(2)
print("Five nutcases battle to the uhh...")
time.sleep(1)
print("not really to the death more like to the slightly damaged...")
time.sleep(2)
print("seriously...")
time.sleep(1)
print("why is there five idiots fighting in the middle of a command window")
time.sleep(3)
print("Welcome to...")
time.sleep(4)
print("~~~~~~~~~~\ngame.jpeg\n~~~~~~~~~~")
time.sleep(2)

#Input 1: Gamemode
gamemode = 0
while gamemode < 1 or gamemode > 4:
    gamemode = int(input("""Choose a Gamemode!
[1]: Singleplayer
[2]: Multiplayer
[3]: Simulation 1
[4]: Simulation 2"""))
    if gamemode < 1 or gamemode > 4:
        print("\nyou're not funny\n")
        time.sleep(1)

#Input 2: Character Selection
def charselect():
    char = 0
    while char < 1 or char > 6:
        char = int(input("""[1]: Wildfire the Pyromancer
[2]: Cleo the Healer
[3]: B.Y.O. the Computer Virus
[4]: Liz the Scientist
[5]: Pylon the Tank"""))
        if char < 1 or char > 6:
            print("\nyou're still not funny\n")
            time.sleep(1)
        else:
            return char
char1 = 0
char2 = 0
charList = ["Wildfire the Pyromancer", "Cleo the Healer", "B.Y.O. the Computer Virus", "Liz the Scientist", "Pylon the Tank", "Mr Dileen the Absolute Hypergod"]
if gamemode == 1:
    print("\n\nSelect your character!\n")
    time.sleep(1)
    char1 = charselect()
    char2 = random.randint(1, 5)
elif gamemode == 2:
    print("\n\nPLAYER ONE Select your character!\n")
    time.sleep(1)
    char1 = charselect()
    time.sleep(1)
    print("\n\nPLAYER TWO Select your character!\n")
    time.sleep(1)
    char2 = charselect()
else:
    char1 = random.randint(1, 5)
    char2 = random.randint(1, 5)

combination = [char1, char2]
combination.sort()
nameList = ["A friendly playfight begins!", "Time to fight fire with fire!", "Two rivals face each other on the battlefield...", "What a bad memory.", "Two Mistakes.", "A Petty Argument.", "Neither of these people know each other but they don't like each other", "Creator vs Creation.", "Absolutely Electric.", "Deja Vu.", "You're screwed.", "There's an IMPOSTER among us!"]
time.sleep(0.5)
print("BATTLE!")
time.sleep(1)
print(charList[char1-1]+"\n\nVS\n\n"+charList[char2-1])
time.sleep(1)

time.sleep(1)
print("\nBEGIN")
print("\n------------------------------------\n")
inGame = True
# [HP, Attack, Defense, Intellect] 
stats = [[180, 10, 10, 3], [240, 7, 12, 2], [120, 18, 6, 7], [150, 6, 14, 20], [280, 13, 14, 15], [999, 999, 999, 999]]
turn = 1
playerControl = 0
secondPlayer = 0
p1Charge = 0
p2Charge = 0
damageStorage = 0
rest = False
#Character with higher intellect goes first
if (stats[char1-1])[3] > (stats[char2-1])[3]:
    playerControl = 1
    secondPlayer = 2
elif (stats[char1-1])[3] < (stats[char2-1])[3]:
    playerControl = 2
    secondPlayer = 1
else:
    playerControl = random.randint(1, 2)
#whole bunch of titles
if combination == [1, 2]:
    print("\n'"+nameList[0]+"'\n")
elif combination == [1, 3]:
    print("\n'"+nameList[1]+"'\n")
elif combination == [1, 4]:
    print("\n'"+nameList[2]+"'\n")
elif combination == [1, 5]:
    print("\n'"+nameList[3]+"'\n")
elif combination == [2, 3]:
    print("\n'"+nameList[4]+"'\n")
elif combination == [2, 4]:
    print("\n'"+nameList[5]+"'\n")
elif combination == [2, 5]:
    print("\n'"+nameList[6]+"'\n")
elif combination == [3, 4]:
    print("\n'"+nameList[7]+"'\n")
elif combination == [3, 5]:
    print("\n'"+nameList[8]+"'\n")
elif combination == [4, 5]:
    print("\n'"+nameList[9]+"'\n")
elif combination[0] == combination[1]:
    print("\n'"+nameList[11]+"'\n")
else:
    print("\n'"+nameList[10]+"'\n")

def moveselect(x):
    move = 0
    while move < 1 or move > 4:
        if x == 1:
            move = int(input("""[1]: Pistol Shot
[2]: Blaze Barrage
[3]: Firewall
[4]: Charge"""))
        elif x == 2:
            move = int(input("""[1]: High Heel Sneaker(tm) Kick
[2]: Starlight Heal
[3]: Navigator's Shield
[4]: Charge"""))
        elif x == 3:
            move = int(input("""[1]: Glitch
[2]: Malware Bombs
[3]: Defensive Mutation
[4]: Charge"""))
        elif x == 4:
            move = int(input("""[1]: Metallic Strike
[2]: Random Chemicals
[3]: Holographic Shield
[4]: Charge"""))
        elif x == 5:
            move = int(input("""[1]: Thunderstrike
[2]: Energy Cannon
[3]: Cyborg Defense
[4]: Charge"""))
        elif x == 6:
            move = int(input("""[1]: instakill opponent
[2]: instakill opponent
[3]: negate all damage
[4]: why would you even need to charge at this point"""))
        if move < 1 or move > 6:
            print("\nstop\n")
            time.sleep(1)
        else:
            return move

hp = [(stats[char1-1])[0], (stats[char2-1])[0]]
moves = [["Pistol Shot", "High Heel Sneaker(tm) Kick", "Glitch", "Metallic Strike", "Thunderstrike", "instakill opponent"], ["Blaze Barrage", "Starlight Heal", "Malware Bombs", "Random Chemicals", "Energy Cannon", "instakill opponent"], ["Firewall", "Navigator's Shield", "Defensive Mutation", "Holographic Shield", "Cyborg Defense", "negate all damage"] ]
p1Move = 0
p2Move = 0
damage = 0
p1Def = False
p2Def = False
heal = 0
time.sleep(1.5)
multiplier = 0
winningPlayer = ["Winning Player"]
winningChar = ["Winning Character"]
losingPlayer = ["Losing Player"]
losingChar = ["Losing Character"]
turnCount = ["Turn Count"]
if gamemode <= 2:
    while inGame == True:
        for i in range(2):
            if playerControl == 1 and hp[0] != 0:
                p1Def = False
                print("PLAYER ONE! GO!")
                time.sleep(1)
                print("\nHP: "+str(int(hp[0]))+"/"+str(int((stats[char1-1])[0])))
                p1Move = moveselect(char1)
                if p1Move == 1:
                    multiplier = random.randint(25, 35)
                    damage = (((stats[char1-1])[1])*((p1Charge/2)+1)*(multiplier/10))/(((stats[char2-1])[2])/10)
                    damage = round(damage)
                    if p2Def == True:
                        if char2 == 6 or (char1 == 3 and char2 == 1):
                            damage = 0
                            
                        hp[1] = hp[1]-(damage/2)
                    else:
                        hp[1] = hp[1]-damage
                    time.sleep(0.5)
                    print("PLAYER ONE used "+(moves[0])[char1-1]+"!")
                    time.sleep(0.5)
                    if p2Def == True:
                        if char2 == 6 or (char1 == 3 and char2 == 1):
                            print("Not even a scratch!")
                        else:
                            print("PLAYER TWO blocked it!")       
                    print("It dealt "+str(damage)+" damage!")
                    if p1Charge >= 1:
                        time.sleep(0.5)
                        print("All of PLAYER ONE's energy was used up!")
                    time.sleep(1.5)
                    p1Charge = 0
                elif p1Move == 3:
                    p1Def = True
                    print("PLAYER ONE used "+(moves[2])[char1-1]+"!")
                    time.sleep(1)
                    print("Their defense increased significantly!")
                    time.sleep(1.5)
                elif p1Move == 4:
                    p1Charge += 1
                    print("PLAYER ONE absorbed energy...")
                    time.sleep(1.5)
    # HOOOOOO BOY
                elif p1Move == 2:
                    if char1 == 2:
                        heal = random.randint(10, 25)
                        print("PLAYER ONE used "+(moves[1])[char1-1]+"!")
                        time.sleep(1)
                        hp[0] += heal
                        if hp[0] > (stats[char1-1])[0]:
                            hp[0] = (stats[char1-1])[0]
                        print("They restored "+str(heal)+" health!")
                    elif char1 == 4:
                        multiplier = random.randint(8, 12)
                        damage = (((stats[char1-1])[1])*(multiplier/10))/(((stats[char2-1])[2])/10)
                        damage = round(damage)
                        hp[1] = hp[1]-damage
                        print("PLAYER ONE used "+(moves[1])[char1-1]+"!")
                        time.sleep(0.5)     
                        print("It dealt "+str(damage)+" damage!")
                        heal = random.randint(5, 15)
                        hp[0] += heal
                        if hp[0] > (stats[char1-1])[0]:
                            hp[0] = (stats[char1-1])[0]
                        time.sleep(0.5) 
                        print("They restored "+str(heal)+" health!")
                    else:
                        multiplier = random.randint(15, 75)
                        damage = (((stats[char1-1])[1])*(multiplier/10))/(((stats[char2-1])[2])/10)
                        damage = round(damage)
                        if p2Def == True:
                            if char2 == 6 or (char1 == 3 and char2 == 1):
                                damage = 0
                            
                            hp[1] = hp[1]-(damage/2)
                        else:
                            hp[1] = hp[1]-damage
                        print("PLAYER ONE used "+(moves[1])[char1-1]+"!")
                        time.sleep(0.5)
                        if p2Def == True:
                            if char2 == 6 or (char1 == 3 and char2 == 1):
                                print("Not even a scratch!")
                            else:
                                print("PLAYER TWO blocked it!")    
                        print("It dealt "+str(damage)+" damage!")
                    time.sleep(1.5)
                playerControl = 2
                if hp[1] < 0:
                    hp[1] = 0
                
            elif playerControl == 2 and hp[1] != 0:
                p2Def = False
                if gamemode == 2:
                    print("PLAYER TWO! GO!")
                    time.sleep(1)
                    print("\nHP: "+str(int(hp[1]))+"/"+str(int((stats[char2-1])[0])))
                    p2Move = moveselect(char2)
                else:
                    p2Move = random.randint(1, 4)
                if p2Move == 1:
                    multiplier = random.randint(25, 35)
                    damage = (((stats[char2-1])[1])*((p2Charge/2)+1)*(multiplier/10))/(((stats[char1-1])[2])/10)
                    damage = round(damage)
                    if p1Def == True:
                        if char1 == 6 or (char2 == 3 and char1 == 1):
                            damage = 0
                            
                        hp[0] = hp[0]-(damage/2)
                    else:
                        hp[0] = hp[0]-damage
                    time.sleep(0.5)
                    print("PLAYER TWO used "+(moves[0])[char2-1]+"!")
                    time.sleep(0.5)
                    if p1Def == True:
                        if char1 == 6 or (char2 == 3 and char1 == 1):
                            print("Not even a scratch!")
                        else:
                            print("PLAYER ONE blocked it!")
                    print("It dealt "+str(damage)+" damage!")
                    if p2Charge >= 1:
                        time.sleep(0.5)
                        print("All of PLAYER TWO's energy was used up!")
                    time.sleep(1.5)
                    p2Charge = 0
                elif p2Move == 3:
                    p2Def = True
                    print("PLAYER TWO used "+(moves[2])[char2-1]+"!")
                    time.sleep(1)
                    print("Their defense increased significantly!")
                    time.sleep(1.5)
                elif p2Move == 4:
                    p2Charge += 1
                    print("PLAYER TWO absorbed energy...")
                    time.sleep(1.5)
                elif p2Move == 2:
                    if char2 == 2:
                        heal = random.randint(10, 25)
                        print("PLAYER TWO used "+(moves[1])[char2-1]+"!")
                        time.sleep(1)
                        hp[1] += heal
                        if hp[1] > (stats[char2-1])[0]:
                            hp[1] = (stats[char2-1])[0]
                        print("They restored "+str(heal)+" health!")
                    elif char2 == 4:
                        multiplier = random.randint(8, 12)
                        damage = (((stats[char2-1])[1])*(multiplier/10))/(((stats[char1-1])[2])/10)
                        damage = round(damage)
                        hp[0] = hp[0]-damage
                        print("PLAYER TWO used "+(moves[1])[char2-1]+"!")
                        time.sleep(0.5)     
                        print("It dealt "+str(damage)+" damage!")
                        heal = random.randint(5, 15)
                        hp[1] += heal
                        if hp[1] > (stats[char2-1])[0]:
                            hp[1] = (stats[char2-1])[0]
                        time.sleep(0.5) 
                        print("They restored "+str(heal)+" health!")
                    else:
                        multiplier = random.randint(15, 75)
                        damage = (((stats[char2-1])[1])*(multiplier/10))/(((stats[char1-1])[2])/10)
                        damage = round(damage)
                        if p1Def == True:
                            if char1 == 6 or (char2 == 3 and char1 == 1):
                                damage = 0
                            
                            hp[0] = hp[0]-(damage/2)
                        else:
                            hp[0] = hp[0]-damage
                        print("PLAYER TWO used "+(moves[1])[char2-1]+"!")
                        time.sleep(0.5)
                        if p1Def == True:
                            if char1 == 6 or (char2 == 3 and char1 == 1):
                                print("Not even a scratch!")
                            else:
                                print("PLAYER ONE blocked it!")
                        print("It dealt "+str(damage)+" damage!")
                    time.sleep(1.5)
                playerControl = 1
                if hp[0] < 0:
                    hp[0] = 0
        turn += 1
        if hp[0] == 0 or hp[1] == 0:
            inGame = False

else:
    gameCount = int(input("How many games do you want to simulate?"))
    for i in range(gameCount):
        while inGame == True:
            for i in range(2):
                if playerControl == 1 and hp[0] != 0:
                    p1Def = False
                    if gamemode == 3:
                        if turn%5 == 0:
                            p1Move = 1
                        else:
                            p1Move = 4
                    elif gamemode == 4:
                        if turn%2 == 0:
                            p1Move = 3
                        else:
                            p1Move = random.randint(1, 2)
                    if p1Move == 1:
                        multiplier = random.randint(25, 35)
                        damage = (((stats[char1-1])[1])*((p1Charge/2)+1)*(multiplier/10))/(((stats[char2-1])[2])/10)
                        damage = round(damage)
                        if p2Def == True:
                            if char2 == 6 or (char1 == 3 and char2 == 1):
                                damage = 0
                                
                            hp[1] = hp[1]-(damage/2)
                        else:
                            hp[1] = hp[1]-damage
                        p1Charge = 0
                    elif p1Move == 3:
                        p1Def = True
                    elif p1Move == 4:
                        p1Charge += 1
                    elif p1Move == 2:
                        if char1 == 2:
                            heal = random.randint(10, 25)
                            hp[0] += heal
                            if hp[0] > (stats[char1-1])[0]:
                                hp[0] = (stats[char1-1])[0]
                        elif char1 == 4:
                            multiplier = random.randint(8, 12)
                            damage = (((stats[char1-1])[1])*(multiplier/10))/(((stats[char2-1])[2])/10)
                            damage = round(damage)
                            hp[1] = hp[1]-damage
                            heal = random.randint(5, 15)
                            hp[0] += heal
                            if hp[0] > (stats[char1-1])[0]:
                                hp[0] = (stats[char1-1])[0]
                        else:
                            multiplier = random.randint(15, 75)
                            damage = (((stats[char1-1])[1])*(multiplier/10))/(((stats[char2-1])[2])/10)
                            damage = round(damage)
                            if p2Def == True:
                                if char2 == 6 or (char1 == 3 and char2 == 1):
                                    damage = 0
                                
                                hp[1] = hp[1]-(damage/2)
                            else:
                                hp[1] = hp[1]-damage
                    playerControl = 2
                    if hp[1] < 0:
                        hp[1] = 0
                    
                elif playerControl == 2 and hp[1] != 0:
                    p2Def = False
                    p2Move = random.randint(1, 4)
                    if p2Move == 1:
                        multiplier = random.randint(25, 35)
                        damage = (((stats[char2-1])[1])*((p2Charge/2)+1)*(multiplier/10))/(((stats[char1-1])[2])/10)
                        damage = round(damage)
                        if p1Def == True:
                            if char1 == 6 or (char2 == 3 and char1 == 1):
                                damage = 0
                                
                            hp[0] = hp[0]-(damage/2)
                        else:
                            hp[0] = hp[0]-damage
                        p2Charge = 0
                    elif p2Move == 3:
                        p2Def = True
                    elif p2Move == 4:
                        p2Charge += 1
                    elif p2Move == 2:
                        if char2 == 2:
                            heal = random.randint(10, 25)
                            hp[1] += heal
                            if hp[1] > (stats[char2-1])[0]:
                                hp[1] = (stats[char2-1])[0]
                        elif char2 == 4:
                            multiplier = random.randint(8, 12)
                            damage = (((stats[char2-1])[1])*(multiplier/10))/(((stats[char1-1])[2])/10)
                            damage = round(damage)
                            hp[0] = hp[0]-damage
                            heal = random.randint(5, 15)
                            hp[1] += heal
                            if hp[1] > (stats[char2-1])[0]:
                                hp[1] = (stats[char2-1])[0]
                        else:
                            multiplier = random.randint(15, 75)
                            damage = (((stats[char2-1])[1])*(multiplier/10))/(((stats[char1-1])[2])/10)
                            damage = round(damage)
                            if p1Def == True:
                                if char1 == 6 or (char2 == 3 and char1 == 1):
                                    damage = 0
                                
                                hp[0] = hp[0]-(damage/2)
                            else:
                                hp[0] = hp[0]-damage
                    playerControl = 1
                    if hp[0] < 0:
                        hp[0] = 0
            turn += 1
            if hp[0] == 0 or hp[1] == 0:
                inGame = False
        if hp[0] == 0:
            print("Player 2 ("+charList[char2-1]+") defeated Player 1 ("+charList[char1-1]+") in the span of "+str(turn)+" turns.")
            winningPlayer.append(2)
            winningChar.append(char2)
            losingPlayer.append(1)
            losingChar.append(char1)
            turnCount.append(turn)
            
        if hp[1] == 0:
            print("Player 1 ("+charList[char1-1]+") defeated Player 2 ("+charList[char2-1]+") in the span of "+str(turn)+" turns.")
            winningPlayer.append(1)
            winningChar.append(char1)
            losingPlayer.append(2)
            losingChar.append(char2)
            turnCount.append(turn)
        char1 = random.randint(1, 5)
        char2 = random.randint(1, 5)
        turn = 1
        hp = [(stats[char1-1])[0], (stats[char2-1])[0]]
        inGame = True
    writer.writerow(winningPlayer)
    writer.writerow(winningChar)
    writer.writerow(losingPlayer)
    writer.writerow(losingChar)
    writer.writerow(turnCount)
    
if gamemode <= 2:
    print("\n--------------------------------\n")
    print("THE WINNER IS...")
    time.sleep(2)
    if hp[0] == 0:
        print("PLAYER TWO!!!")
    if hp[1] == 0:
        print("PLAYER ONE!!!")
csvFile.close()