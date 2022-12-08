

def parse_start(msg, start_size):
    buffer = []
    ind = 0
    for i, char in enumerate(msg):
        if char in buffer:
            ind = buffer.index(char)
            buffer = buffer[ind+1:]
        else:
            if len(buffer) == start_size - 1:
                ind = i + 1
                break
        buffer.append(char)

    return msg[ind:], ind

if __name__ == "__main__":
    f = open("input.txt", "r", encoding="utf-8")
    input = f.readlines()[0]

    msg, start_ind = parse_start(input, 4)
    msg, msg_ind = parse_start(input, 14)



    print(f"{len(input)} {start_ind} {msg_ind}")