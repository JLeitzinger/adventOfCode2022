
def readFile(fpath):
    with open(fpath, 'r') as f:
        temp = f.read()
    
    return temp.splitlines()

def parseFile(file):
    divide = file.index('')
    crates = file[0:divide]
    moves = file[divide+1:]
    
    return crates, moves

def parseCrates(crates, n):
    output = []
    remList = ['[', ']', ' ']

    for row in crates:
        temp = parseCrateRow(row, n)
        temp = cleanCrates(temp, remList)
        output.append(temp)
    

    output = transposeCrates(output)
    output = removeEmpty(output)

    return output

def parseCrateRow(rowCrate, n):
    return [rowCrate[i:i+n] for i in range(0, len(rowCrate), n)]

def cleanCrates(crates, remList):
    for rem in remList:
        crates = [x.replace(rem, '') for x in crates]
    
    return crates

def transposeCrates(crates):
    return list(map(list, zip(*crates)))

def removeEmpty(crates):
    output = []

    for crate in crates:
        temp = [x for x in crate if x != '']
        output.append(temp)
    
    return output

def makeCrateDict(crates):
    outputDict = {}

    for crate in crates:
        outputDict[crate[-1]] = crate[:-1]
    
    return outputDict

#### Organize the moves ####
def parseMoves(moves):
    output = []
    temp = [x.split(' ') for x in moves]
    temp = removeExtraWords(temp)

    return temp

def removeExtraWords(moves):
    output = []
    for move in moves:
        output.append([x for x in move if x not in ['move', 'from', 'to']])
    
    return output


#### Engine ####
def moveFrom(crateDict, src):
    pulled = crateDict[src].pop(0)
    return crateDict, pulled

def moveTo(crateDict, dest, val):
    crateDict[dest].insert(0, val)
    return crateDict

def engine(moves, crates):
    for move in moves:

        timesMove = int(move[0])
        fromMove = move[1]
        toMove = move[2]


        for i in range(timesMove):
            crates, val = moveFrom(crates, fromMove)
            crates = moveTo(crates, toMove, val)
            print(f'Moving {val} \nFrom: {fromMove} \nTo: {toMove}')
            
    
    return(crates)






if __name__=='__main__':
    setup = readFile('./Day5/crate.txt')
    
    # Organize the crates data. Creates a dictionary
    # key = crate number
    crates, moves = parseFile(setup)
    crates = parseCrates(crates, 4)
    crates = makeCrateDict(crates)

    #Organize moves
    moves = parseMoves(moves)
    
    # Run the engine

    endPos = engine(moves, crates)

    print(endPos)

    endList = []
    for k, v in endPos.items():
        endList.append(v[0])

    print(endList)