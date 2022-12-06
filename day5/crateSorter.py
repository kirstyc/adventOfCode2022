import re

def getStacks(lines):
    lines.reverse()
    header = lines.pop(0) 
    stacks = []
    positions = []
    for pos, char in enumerate(header):
        if char.isnumeric():
            positions.append(pos)
            stacks.append([])

    for line in lines:
        for i, char in enumerate(line):
            if char.isalpha():
                ind = positions.index(i)
                stacks[ind].append(char)

    return stacks

def moveStack(instruction, stacks, part1 = True):
    ret = re.findall(r'\d+', instruction)
    num = int(ret[0])
    src = int(ret[1]) - 1
    dest = int(ret[2]) - 1
    moving = stacks[src][-1*num:]
    if part1:
        moving.reverse()

    stacks[src] = stacks[src][:-1*num]
    stacks[dest].extend(moving) 

    return stacks

if __name__ == "__main__":
    f = open("input.txt", 'r', encoding='utf-8')
    lines = f.readlines()
    ### part one ###
    stacklines = []
    ilines = []
    delimiterFound = False
    for line in lines:
        # read instructions 
        if delimiterFound:
            ilines.append(line)
        # read stacks
        elif line != '\n':
            stacklines.append(line)
        else:
            delimiterFound = True

    # build stacks 
    stacks = getStacks(stacklines)
    print(stacks)
    # # execute instructions
    for instruction in ilines:
        stacks = moveStack(instruction, stacks, part1=False)

    print(stacks)
    # # read top of stacks
    msg = ''
    for stack in stacks:
        msg += stack[-1]

    print(f"{msg}")

