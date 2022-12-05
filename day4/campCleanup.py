
def parse(msg):
    msg = msg.strip()
    msg = msg.replace('-', ',')
    elf1Low, elf1High, elf2Low, elf2High = msg.split(',')
    elf1 = list(range(int(elf1Low), int(elf1High)+1))
    elf2 = list(range(int(elf2Low), int(elf2High)+1))

    return elf1, elf2

def overlap(elf1, elf2):
    overlap = []
    for i in elf1:
        if i in elf2:
            overlap.append(i)

    return overlap

if __name__ == "__main__":

    # read input 
    f = open("input.txt", "r", encoding="utf-8")
    lines = f.readlines()

    complete = 0 # part one
    total = 0 # part two
    for line in lines:
        # get pairs
        elf1, elf2 = parse(line)
        # find overlap in assignments 
        matches = overlap(elf1, elf2)
        if len(matches) > 0:
            total += 1
        # check if overlap is someone's whole assignment
        if len(matches) == len(elf1) or len(matches) == len(elf2):
            complete +=1

    print(f"complete overlap: {complete}")

    print(f"total overlap: {total}")
    

