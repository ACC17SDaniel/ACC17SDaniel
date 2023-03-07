import pandas
import plotly.express as px
mode = int(input("""Do you want to analyse:
[1] Normal Play
[2] Simulations"""))
if mode == 2:
    df = pandas.read_csv("funny.csv")
    winList = (df.values.tolist())[0]
    winChar = (df.values.tolist())[1]
    loseList = (df.values.tolist())[2]
    loseChar = (df.values.tolist())[3]
    turnCounts = (df.values.tolist())[4]
    hpDifference = (df.values.tolist())[5]
    # Creating dataset
    chars = ['WILDFIRE', 'CLEO', 'BYO',
     'LIZ', 'PYLON']
    players = ['PLAYER 1', "PLAYER 2"]
    dataChar = [0, 0, 0, 0, 0]
    for i in range(len(winChar)):
        dataChar[int(winChar[i]-1)] +=1
    dataPlayer = [0, 0]
    for i in range(len(winList)):
        dataPlayer[int(winList[i]-1)] +=1
    # Creating plot
    fig1 = px.pie(values = dataChar, names = chars)
    fig2 = px.pie(values = dataPlayer, names = players)
    fig3 = px.scatter(x=turnCounts, y=hpDifference)
    # show plot
    fig1.show() 
    fig2.show()
    fig3.show()
elif mode == 1:
    df = pandas.read_csv("livefunnyreaction.csv")
    damageP1 = (df.values.tolist())[0]
    damageP2 = (df.values.tolist())[1]
    winPlayer = int(((df.values.tolist())[2])[0])
    p1Attack = (df.values.tolist())[3]
    p2Attack = (df.values.tolist())[4]
    damage = damageP1+damageP2
    turns = []
    player = []
    # Creating dataset
    for i in range(len(damageP1)):
        turns.append(i+1)
    for j in range(len(damageP2)):
        turns.append(j+1)
    for k in range(len(damageP1)):
        player.append("Player 1")
    for l in range(len(damageP1)):
        player.append("Player 2")
    # Creating plot
    fig1 = px.scatter(x=turns, y=damage, color=player)
    # show plot
    fig1.show()
    def zeroCheck(num):
        if num == 0 or num == float("nan"):
            return False
        else:
            return True
    damageP1 = list(filter(zeroCheck, damageP1))
    damageP1.sort()
    damageP2 = list(filter(zeroCheck, damageP2))
    damageP2.sort()
    damageP2.remove(1)
    damageP1 = [x for x in damageP1 if pandas.isnull(x) == False]
    damageP2 = [y for y in damageP2 if pandas.isnull(y) == False]
    p1Attack = [z for z in p1Attack if pandas.isnull(z) == False]
    p2Attack = [a for a in p2Attack if pandas.isnull(a) == False]
    p1Attack.sort()
    p1Attack.append(0)
    p2Attack.sort()
    p2Attack.append(0)
    mean1 = round((sum(damageP1))/(len(damageP1)), 2)
    mean2 = round((sum(damageP2))/(len(damageP2)), 2)
    dmgFrq1 = round((len(damageP1)/(len(turns)/2))*100, 2)
    dmgFrq2 = round((len(damageP2)/(len(turns)/2))*100, 2)
    median1 = 0
    median2 = 0
    if len(damageP1)%2 == 0:
        median1 = (damageP1[int(len(damageP1)/2)]+damageP1[int((len(damageP1)/2)+1)])/2
    else:
        median1 = damageP1[int((len(damageP1)//2)+1)]
    if len(damageP2)%2 == 0:
        median2 = (damageP2[int(len(damageP2)/2)]+damageP2[int((len(damageP2)/2)+1)])/2
    else:
        median2 = damageP2[int((len(damageP2)//2)+1)]
    mode1 = 0
    highFrq = 0
    frq = 0
    marker = 0
    for m in range(len(p1Attack)):
        if p1Attack[m] != marker:
            if frq > highFrq:
                mode1 = p1Attack[m-1]
                highFrq = frq
            frq = 1
            marker = p1Attack[m]
        else:
            frq += 1
    mode2 = 0
    highFrq = 0
    frq = 0
    marker = 0
    for n in range(len(p2Attack)):
        if p2Attack[n] != marker:
            if frq > highFrq:
                mode2 = p2Attack[n-1]
                highFrq = frq
            frq = 1
            marker = p2Attack[n]
        else:
            frq += 1
    print("The winner was: Player "+str(winPlayer)+"\nThe mean damage outputted by Player 1 was: "+str(mean1)+"\nThe mean damage outputted by Player 2 was: "+str(mean2)+"\nThe median damage outputted by Player 1 was: "+str(median1)+"\nThe median damage outputted by Player 2 was: "+str(median2)+"\nPlayer 1 dealt damage "+str(dmgFrq1)+"% of the time\nPlayer 2 dealt damage "+str(dmgFrq2)+"% of the time\nThe most used move by Player 1 is: Move "+str(int(mode1))+"\nThe most used move by Player 2 is: Move "+str(int(mode2)))