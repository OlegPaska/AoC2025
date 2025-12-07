lines = []

with open("q7/in.txt") as f:
    for l in f:
        lines.append(l.strip())


def beam(x,y):
    global splits
    global lines
    char = lines[y][x]
    while char != '^':
        if y >= len(lines)-1: return
        if lines[y][x] == '.': lines[y] = lines[y][:x] + '|' + lines[y][x+1:]
        else: 
            print("what")
        y += 1
        char = lines[y][x]
    if char == '^':
        #print(f"{x}, {y}")
        splits += 1
        if lines[y][x-1] != '|':
            beam(x-1, y)
        if lines[y][x+1] != '|':
            beam(x+1, y)


splits = 0
beam(lines[0].index('S'), 1)

res = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '^' and lines[y-1][x] == '|':
            res += 1
            print(x,y)
print(f"res: {res}")

#for l in lines:print(l)
#print(splits)

