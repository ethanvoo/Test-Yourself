import csv
import os

file_path = "LeaderBoard.csv"
if not os.path.exists(file_path):
    file = open("LeaderBoard.csv","w")
    file.write("Random Dice Leader board!\n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.close()

How_Meny_Correct = 42 #how meny questions acc corect
place = 11 #place is automatically 11 bc we only be printing the first ten from the csv


i = 1
z = 1
file = open("LeaderBoard.csv","r")
reader = csv.reader(file)
title = list(reader)
while z != 11:
    if i != 1:
        print(z)
        scoreLead = str(title[z][0]) # grabs the score from the positon of the leader board i is at
        try:
            scoreLead = int(scoreLead)
        except:
            scoreLead = 0
        if How_Meny_Correct  > scoreLead:
            place = place - 1 # your score is bigger than the one copied from the csv file then you go up a place
        elif How_Meny_Correct < scoreLead and i == 11 and place == 11:
            print("not on the leaderboard this time")
        z = z + 1
    i = i + 1
file.close()


How_Meny_Correct = str(How_Meny_Correct)
file = open("LeaderBoard.csv","r")
x = 0
y = 0
v = 0
j = 0
tmp = [[" "," "],
        [" "," "],
        [" "," "],
        [" "," "],
        [" "," "],
        [" "," "],
        [" "," "],
        [" "," "],
        [" "," "],
        [" "," "],
        [" "," "],
        [" "," "]]
    
#its called "namefrfr" bc there used to be a checker making your name only 3 charaters long
namefrfr = input("Enter your name: ")
reader = csv.reader(file)
title = list(reader)
Row = str(title[0][0])
tmp[0][0] = Row

#the omega if statement puts your score on the array to copy to the csv
if place == 1:
    tmp[1][0] = How_Meny_Correct
    tmp[1][1] = namefrfr
    v = 2
    o = 1
    while j != 9:
        tmp[v][0] = title[o][0]
        tmp[v][1] = title[o][1]
        v = v + 1
        j = j + 1
        o = o + 1
elif place == 2:
    v = 3
    o = 2
    x = 1
    while x != place:
        tmp[x][0] = title[x][0]
        tmp[x][1] = title[x][1]
        x = x + 1 
    tmp[place][0] = How_Meny_Correct
    tmp[place][1] = namefrfr
    while j != 7:
        tmp[v][0] = title[o][0]
        tmp[v][1] = title[o][1]
        v = v + 1
        j = j + 1
        o = o + 1
elif place == 3:
    v = 4
    o = 3
    x = 1
    while x != place:
        tmp[x][0] = title[x][0]
        tmp[x][1] = title[x][1]
        x = x + 1 
    tmp[place][0] = How_Meny_Correct
    tmp[place][1] = namefrfr
    while j != 6:
        tmp[v][0] = title[o][0]
        tmp[v][1] = title[o][1]
        v = v + 1
        j = j + 1
        o = o + 1
elif place == 4:
    v = 5
    o = 4
    x = 1
    while x != place:
        tmp[x][0] = title[x][0]
        tmp[x][1] = title[x][1]
        x = x + 1 
    tmp[place][0] = How_Meny_Correct
    tmp[place][1] = namefrfr
    while j != 5:
        tmp[v][0] = title[o][0]
        tmp[v][1] = title[o][1]
        v = v + 1
        j = j + 1
        o = o + 1
elif place == 5:
    v = 6
    o = 5
    x = 1
    while x != place:
        tmp[x][0] = title[x][0]
        tmp[x][1] = title[x][1]
        x = x + 1 
    tmp[place][0] = How_Meny_Correct
    tmp[place][1] = namefrfr
    while j != 4:
        tmp[v][0] = title[o][0]
        tmp[v][1] = title[o][1]
        v = v + 1
        j = j + 1
        o = o + 1
elif place == 6:
    v = 7
    o = 6
    x = 1
    while x != place:
        tmp[x][0] = title[x][0]
        tmp[x][1] = title[x][1]
        x = x + 1 
    tmp[place][0] = How_Meny_Correct
    tmp[place][1] = namefrfr
    while j != 3:
        tmp[v][0] = title[o][0]
        tmp[v][1] = title[o][1]
        v = v + 1
        j = j + 1
        o = o + 1
elif place == 7:
    v = 8
    o = 7
    x = 1
    while x != place:
        tmp[x][0] = title[x][0]
        tmp[x][1] = title[x][1]
        x = x + 1 
    tmp[place][0] = How_Meny_Correct
    tmp[place][1] = namefrfr
    while j != 2:
        tmp[v][0] = title[o][0]
        tmp[v][1] = title[o][1]
        v = v + 1
        j = j + 1
        o = o + 1
elif place == 8:
    v = 9
    o = 8
    x = 1
    while x != place:
        tmp[x][0] = title[x][0]
        tmp[x][1] = title[x][1]
        x = x + 1 
    tmp[place][0] = How_Meny_Correct
    tmp[place][1] = namefrfr
    while j != 1:
        tmp[v][0] = title[o][0]
        tmp[v][1] = title[o][1]
        v = v + 1
        j = j + 1
        o = o + 1
elif place == 9:
    v = 10
    o = 9
    x = 1
    while x != place:
        tmp[x][0] = title[x][0]
        tmp[x][1] = title[x][1]
        x = x + 1 
    tmp[place][0] = How_Meny_Correct
    tmp[place][1] = namefrfr
    tmp[v][0] = title[o][0]
    tmp[v][1] = title[o][1]
elif place == 10:
    v = 11
    o = 10
    x = 1
    while x != place:
        tmp[x][0] = title[x][0]
        tmp[x][1] = title[x][1]
        x = x + 1 
    tmp[place][0] = How_Meny_Correct
    tmp[place][1] = namefrfr

file.close()
file = open("Leaderboard.csv","w")
y = 0
for row in tmp:
    data = str(row) 
    RawData = data.replace('[','')
    RawData = RawData.replace(' ','')
    RawData = RawData.replace(']','')
    RawData = RawData.replace("'",'')        
    newRec = RawData + '\n'
    file.write(newRec)
    y = y + 1
file.close()