

def getPriority(val):
    prioVal = val.pop()
    prioVal = ord(prioVal) - 96

    if prioVal > 0:
        return prioVal
    else:
        return prioVal + 58

with open("./Day3/ruck.txt", "r") as f:
    temp = f.read()


rucks = temp.splitlines()

prioList = []

for i in range(0,len(rucks)):
    if (i%3==0):
        temp = [set(x) for x in rucks[i:i+3]]

        badge = set.intersection(*temp)
        temp = getPriority(badge)
        prioList.append(temp)
    else:
        pass

print(sum(prioList))
