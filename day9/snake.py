from numpy import sign

def distance(x1, y1, x2, y2):
    deltaX = x2 - x1
    deltaY = y2 - y1 

    dist = (deltaX**2 + deltaY**2)**0.5
    return dist

def move(dir, x, y):
    if dir == 'R':
        x += 1

    elif dir == 'L':
        x -= 1
    
    elif dir == 'U':
        y += 1

    else:
        y -= 1

    return [x,y] 

def tail_move(head_x, head_y, tail_x, tail_y):
    dist = distance(head_x, head_y, tail_x, tail_y)
    if dist >= 2:
        delta_x = head_x - tail_x
        delta_y = head_y - tail_y
        tail_x += sign(delta_x)
        tail_y += sign(delta_y)

    return [tail_x, tail_y]

def get_command(line):
    line = line.strip()
    ret = line.split()
    dir = ret[0]
    length = int(ret[1])
    return dir, length


        
if __name__ == "__main__":
    # f = open('input_ex.txt', 'r', encoding='utf-8')
    f = open('input.txt', 'r', encoding='utf-8')
    # f = open('input_9.txt', 'r', encoding='utf-8')
    lines = f.readlines()

    ### part one ###
    head = [[0,0]]
    tail = [[0,0]]

    t = 0
    for line in lines:
        dir, length = get_command(line)
        for i in range(length):
            head.append(move(dir, *head[t]))
            if distance(*tail[t], *head[t+1]) > 2**0.5:
                tail.append(head[t])
            else:
                tail.append(tail[t])

            t += 1

    # remove duplicates in tail 
    tail_unique = [str(i) for i in tail]
    tail_unique = [*set(tail_unique)]
    print(f"{len(tail_unique)}")

    ### part two ###
    origin = [0,0]
    snake = [ origin for i in range(10) ]
    tail_pos = {}
    for line in lines:
        dir, length = get_command(line)
        for i in range(length):
            for ind in range(len(snake)):
                if ind == 0: # head move
                    snake[ind] = move(dir, *snake[ind])
                else:
                    snake[ind] = tail_move(*snake[ind-1], *snake[ind])

                if ind == len(snake)-1: # last tail move
                    key = str(snake[ind])
                    if key not in tail_pos:
                        tail_pos[key] = 1
                    else:
                        tail_pos[key] += 1

    print(len(tail_pos))




