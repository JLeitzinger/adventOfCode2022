
with open('./Day3/ruck.txt', 'r') as f:
    temp = f.read()

rucks = temp.splitlines()

print(rucks)

def halfPoint(string):
    return round(len(string)/2)

sameList = []
prioList = []


for ruck in rucks:
    #split them
    split = halfPoint(ruck)

    first = set(ruck[:split])
    second = set(ruck[split:])

    sameList.append(first.intersection(second))

sameSave = []

for prio in sameList:
    prioLetter = prio.pop()
    sameSave.append(prioLetter)
    prioVal = ord(prioLetter) - 96
    
    if prioVal > 0:
        prioList.append(prioVal)
    else:
        prioVal+= 58
        prioList.append(prioVal)

sum(prioList)

