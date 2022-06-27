setofchar = ["A","B","C","D","E"]
listofnumber  = []
for i in range(1000,10000):
    listofnumber.append(i)
#print(listofnumber)
def char():
    global roundroundround1
    roundroundround1 = 0
    global roundroundround2
    roundroundround2 = 0
    global roundroundround3
    roundroundround3 = 0
    i = 0
    b = 0
    for nummong in range(len(setofchar)):
        i = 0
        x = 0
        for j in range(len(setofchar)):
            i = 0
            x = 0
            for som in (listofnumber):
                print(setofchar[b],end = "")
                print(setofchar[i],end = "")
                print(listofnumber[x],end = ", ")
                x += 1
                roundroundround1 += 1
            i += 1
            roundroundround2 += 1
        b += 1
        roundroundround3 += 1
char()
print("\nThe number in list = ",roundroundround1)
