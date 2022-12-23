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

    opp = ord(turn[0]) - 65
    res = ord(turn[1]) - 88

    print(opp)
    print(res)

    if res == 1:
        oppRes = [1,2,3]
        result = oppRes[opp] + draw
        results.append(result)

    elif res == 0:
        oppRes = [3, 1, 2]
        result = oppRes[opp] + lose
        results.append(result)
    
    else:
        oppRes = [2, 3, 1]
        result = oppRes[opp] + win
        results.append(result)

print(results)

endResult = sum(results)
print(f'The Total for all rounds: {endResult}')