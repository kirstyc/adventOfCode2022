ROCK = 1
PAPER = 2
SCISSORS = 3
LOSE = 0
DRAW = 3
WIN = 6

points = {
    'X': ROCK,
    'Y': PAPER, 
    'Z': SCISSORS,
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS
}

### part two ###
lose = 'X'
draw = 'Y'
win  = 'Z'

def fight(opponent, me):
    result = LOSE
    me = points[me]
    opp = points[opponent]

    if me == ROCK and opp == SCISSORS:
        result = WIN
    elif me == SCISSORS and opp == ROCK:
        result =  LOSE
    elif (me > opp):
        result = WIN
    elif (me == opp):
        result = DRAW

    return result + me 

def fightTwo(opp, resultLabel):
    opp = points[opp]
    result = WIN
    if resultLabel == lose:
        result = LOSE
        if opp == ROCK:
            me = SCISSORS
        else:
            me = opp - 1
    
    elif resultLabel == draw:
        result = DRAW
        me = opp

    else:
        if opp == SCISSORS:
            me = ROCK
        else:
            me = opp + 1

    return me + result

if __name__=="__main__":
    # get input 
    f = open("input.txt", "r", encoding="utf-8")
    guide = f.readlines()

    #### part one #####
    total = 0
    for line in guide:
        opp, me = line.split()
        score = fight(opp, me)
        total += score 

    print(f"{len(guide)} {score} {total}")

    #### part two #####
    total = 0
    for line in guide:
        opp, me = line.split()
        score = fightTwo(opp, me)
        total += score 

    print(f"{len(guide)} {score} {total}")

