def readFile(filePath:str):
    with open(filePath, 'r') as f:
        temp = f.read()
    
    temp = temp.splitlines()
    return temp

def parseAssignments(assignments:list[str]):
    a1 = []
    a2 = []
    for assign in assignments:
        a = assign.split(',')
        t1 = a[0].split('-')
        t2 = a[1].split('-')
        t1 = [int(x) for x in t1]
        t2 = [int(x) for x in t2]

        a1.append(t1)
        a2.append(t2)

    return a1, a2

def overlap(a1, a2):
    overList = []

    for a1, a2 in zip(a1, a2):

        a1Check = (a1[0]>=a2[0]) & (a1[1]<=a2[1])
        a2Check = (a2[0]>=a1[0]) & (a2[1]<=a1[1])
        if (a1Check):
            overList.append(True)
        elif (a2Check):
            overList.append(True)
        else:
            overList.append(False)
    
    print('The Number of complete overlap:')
    print(sum(overList))

def anyOverlap(a1, a2):
    overList = []

    for a1, a2 in zip(a1, a2):
        a1Check = (a1[0]>=a2[0]) & (a1[0]<=a2[1])
        a2Check = (a2[0]>=a1[0]) & (a2[0]<=a1[1])

        if(a1Check | a2Check):
            overList.append(True)
        else:
            overList.append(False)

    print('\nThe Number of any overlaps:')
    print(sum(overList))

if __name__=='__main__':
    print('Running Main')
    assignments = readFile('./Day4/cleaning.txt')

    print('Read in Assignments')
    a1, a2 = parseAssignments(assignments)

    print('Running set analysis')
    overlap(a1, a2)
    anyOverlap(a1, a2)

