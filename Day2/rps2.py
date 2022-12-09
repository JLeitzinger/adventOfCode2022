'''
a:rock
b:paper
c:scissors

x:rock
y:paper
z:scissors
'''
from aenum import MultiValueEnum

class Action(MultiValueEnum):
    Rock = 'A', 'X'
    Paper = 'B', 'Y'
    Scissors = 'C', 'Z'


with open(f'./Day2/rps.txt', 'r') as f:
    guide = f.read()

turns = [x.split(' ') for x in guide.splitlines()]
results = []

for turn in turns:
    opp = Action(turn[0])
    me = Action(turn[1])

    if opp == me:
        results.append('draw')
    elif opp == Action.Rock:
        if me == Action.Scissors:
            results.append('lose')
        else:
            results.append('win')
    elif opp == Action.Paper:
        if me == Action.Rock:
            results.append('lose')
        else:
            results.append('win')
    else:
        if me == Action.Paper:
            results.append('lose')
        else:
            results.append('win')

print(results)
    
