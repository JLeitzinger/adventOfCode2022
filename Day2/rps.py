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

win = 6
lose = 0
draw = 3

for turn in turns:

    opp = Action(turn[0])
    me = Action(turn[1])
    choicePoints = ord(turn[1]) - 87

    if opp == me:
        result = choicePoints + draw
        results.append(result)

    elif opp == Action.Rock:
        if me == Action.Scissors:
            result = choicePoints + lose
            results.append(result)
        else:
            result = choicePoints + win
            results.append(result)
    elif opp == Action.Paper:
        if me == Action.Rock:
            result = choicePoints + lose
            results.append(result)
        else:
            result = choicePoints + win
            results.append(result)
    else:
        if me == Action.Paper:
            result = choicePoints + lose
            results.append(result)
        else:
            result = choicePoints + win
            results.append(result)

print(results)

endResult = sum(results)
print(f'The Total for all rounds: {endResult}')