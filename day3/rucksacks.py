
def sackSplit(itemLine):
    # remove whitespace
    itemLine = itemLine.strip()
    midpoint = len(itemLine)//2
    comp1 = itemLine[:midpoint]
    comp2 = itemLine[midpoint:]

    return comp1, comp2

def findSame(comp1, comp2):
    for itemChar in comp1:
        if itemChar in comp2:
            return itemChar

def findSames(arr1, arr2):
    sames = []
    for item in arr1:
        if item in arr2:
            if item not in sames:
                sames.append(item)

    return sames

def getValue(item):
    if item >= 'a' and item <= 'z':
        start = ord('a')
        offset = 1
    else:
        start = ord('A')
        offset = 27

    val = ord(item) - start + offset
    return val


if __name__=="__main__":
    # get input 
    f = open("rucksacks.txt", "r", encoding="utf-8")
    sacks = f.readlines()

    total = 0
    for line in sacks:
        comp1, comp2 = sackSplit(line)
        match = findSame(comp1, comp2)
        val = getValue(match)
        total += val

    print(f"{total}")

    ### part two ###
    total = 0
    sizeGroups = 3

    numGroups = len(sacks)//sizeGroups
    for i in range (numGroups):
        ind = i*sizeGroups
        matches = findSames(sacks[ind].strip(), sacks[ind+1].strip())
        if len(matches) > 1:
            result = findSame(matches, sacks[ind+2].strip())
        else:
            result = match[0]
        
        total += getValue(result)

    print(f"{total}")
    
