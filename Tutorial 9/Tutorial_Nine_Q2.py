def rectAreaMinus(tempTupList):
    
    global totalAreaMinus
    tempTup = tempTupList[0]
    tempTupList.remove(tempTup)
    if not tempTupList:
         return 
    for i in range(len(tempTupList)):
        if (tempTupList[i][0] >= tempTup[0] and tempTupList[i][0] <= tempTup[2] and tempTupList[i][1] >= tempTup[1] and tempTupList[i][1] <= tempTup[3] and tempTupList[i][2] >= tempTup[0] and tempTupList[i][2] <= tempTup[2] and tempTupList[i][3] >= tempTup[1] and tempTupList[i][3] <= tempTup[3]):
            temp = [tempTupList[i][0], tempTupList[i][1], tempTupList[i][2] - tempTupList[i][0], tempTupList[i][3] - tempTupList[i][1]]
            totalAreaMinus += rectArea(tuple(temp))
            continue
        elif tempTupList[i][0] >= tempTup[0] and tempTupList[i][0] <= tempTup[2] and tempTupList[i][1] >= tempTup[1] and tempTupList[i][1] <= tempTup[3]:
            temp = [tempTupList[i][0], tempTupList[i][1], tempTup[2]-tempTupList[i][0], tempTup[3]-tempTupList[i][1]]
            totalAreaMinus += rectArea(tuple(temp))
            
        elif tempTupList[i][2] >= tempTup[0] and tempTupList[i][2] <= tempTup[2] and tempTupList[i][3] >= tempTup[1] and tempTupList[i][3] <= tempTup[3]:
            temp = [tempTup[0], tempTup[1], tempTupList[i][2] - tempTup[0], tempTupList[i][3] - tempTup[1]]
            totalAreaMinus += rectArea(tuple(temp))
            
        
        elif tempTupList[i][0] >= tempTup[0] and tempTupList[i][0] <= tempTup[2] and tempTupList[i][3] >= tempTup[1] and tempTupList[i][3] <= tempTup[3]:
            temp = [tempTupList[i][0], tempTupList[i][1], tempTup[2]-tempTupList[i][0], tempTupList[i][3] - tempTup[1]]
            totalAreaMinus += rectArea(tuple(temp))
            
        elif tempTupList[i][2] >= tempTup[0] and tempTupList[i][2] <= tempTup[2] and tempTupList[i][1] >= tempTup[1] and tempTupList[i][1] <= tempTup[3]:
            temp = [tempTup[0], tempTup[1], tempTupList[i][2] - tempTup[0], tempTup[3] - tempTupList[i][1]]
            totalAreaMinus += rectArea(tuple(temp))
            
    rectAreaMinus(tempTupList)

def rectArea(r):
    return r[2]*r[3]

def defTuple(temp):
    tempTup = [temp[0], temp[1], temp[0] + temp[2], temp[1] + temp[3]]
    return tuple(tempTup)

num=int(input())
l = []
lq = []
totalArea = 0
totalAreaMinus = 0
for i in range (num):
    lin=input()
    line=lin.split(" ")
    numb=[int(item) for item in line]
    tup=tuple(numb)
    totalArea += rectArea(tup)
    lq.append(defTuple(tup))

rectAreaMinus(lq)

print(totalArea - totalAreaMinus)  
