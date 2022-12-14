
with open('./Day1/PartOne/elfCarry.txt', 'r') as f:
    elfCalories = f.read()

elfList = elfCalories.splitlines()

def elfParse(elfList):
    elfGrouped = [[]]
    elf = 0

    for item in elfList:
        if item == '':
            elfGrouped.append([])
            elf+=1
        else:
            elfGrouped[elf].append(int(item))
    
    return(elfGrouped)

elfGroups = elfParse(elfList)
    

elfCarry = [sum(x) for x in elfGroups]
elfCarry.sort(reverse=True)


print(f'The max carries calories is: {max(elfCarry)}')
print(f'The sum of the top 3 elvs is: {sum(elfCarry[:3])}')