afabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numberoflist = len(afabet)
def numberone():
    i = 0
    global roundofmemberinlistone
    roundofmemberinlistone = 0
    for x in range(numberoflist) :
        print(afabet[i], end = ',')
        i += 1
        roundofmemberinlistone += 1
def numbertwo():
    i = 0
    b = 0
    global roundofmemberinlisttwo
    roundofmemberinlisttwo = 0
    for y in range(numberoflist):
        i = 0
        for y in range(numberoflist) :
            print(afabet[b], end = '')
            print(afabet[i], end = ',')
            i += 1
            roundofmemberinlisttwo += 1
        b += 1
        roundofmemberinlisttwo += 1
def numberroiA():
    i = 0
    b = 0
    j = 0
    global roundofmemberinlistthree
    roundofmemberinlistthree = 0
    for y in range(numberoflist):
        i = 0
        j = 0
        for y in range(numberoflist):
            i = 0
            for x in range(numberoflist) :
                print(afabet[b], end = '')
                print(afabet[j], end = '')
                print(afabet[i], end = ',')
                i += 1
                roundofmemberinlistthree += 1
            j += 1
            roundofmemberinlistthree += 1
        b += 1
        roundofmemberinlistthree += 1
print("The members in the set = {")
numberone()
print("\n")
numbertwo()
print("\n")
numberroiA()
print("}")
print("\nNumber of members in a list = ",roundofmemberinlistthree)
