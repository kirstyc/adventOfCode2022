

if __name__=="__main__":
    # input
    f = open("calories.txt", 'r', encoding='utf-8')
    lines = f.readlines()

    ###### part one ######
    # find maximum 
    subtotal = 0
    max = 0
    for line in lines:
        if line.strip(): # not empty line 
            subtotal += int(line)
        else:
            if subtotal > max:
                print(f"subtotal {subtotal}")
                max = subtotal
            subtotal = 0

    print(f"max {max}")

    ###### part two ######
    # find sum of top 3
    # reset
    subtotal = 0
    max = 0
    calories = []
    for line in lines:
        if line.strip(): # not empty line 
            subtotal += int(line)
        else:
            calories.append(subtotal)
            subtotal = 0

    # find top 3 
    calories.sort()
    total = sum(calories[-3:])

    print(f"{calories} total {total}")
    

