import numpy as np 

if __name__ == "__main__":
    # f = open("input_baby.txt", "r", encoding = "utf-8")
    # f = open("input_ex.txt", "r", encoding = "utf-8")
    f = open("input.txt", "r", encoding = "utf-8")
    lines = f.readlines()

    reg = [1]
    cycle = 0

    for line in lines:
        ret = line.strip().split()
        instruction = ret[0]

        if instruction == 'noop':
            reg.append(reg[cycle])
            cycle += 1

        else:
            addr = int(ret[1])
            reg.append(reg[cycle])
            reg.append(reg[cycle]+addr)
            cycle += 2

        # print(f"{reg} /t {cycle}")

    clks =[20,60,100,140,180,220]
    sum = 0
    for clk in clks:
        signal = clk*reg[clk-1]
        sum += signal 
        print(signal)

    print(sum)

    pixels = ''
    rows = [0,40,80,120,160,200]
    for i in rows:
        row = np.asarray(reg[i:i+40],dtype=int)
        row += i
        reg[i:i+40] = row.tolist()

    for i in range (len(reg)):
        if i >= reg[i]-1 and i <= reg[i]+1:
            pixel = '#'
        else:
            pixel = '.'
        pixels += pixel
    
    # resize 
    pixels = [pixels[i:i+40] for i in rows]
    for row in pixels:
        print(row)
        

        

    
