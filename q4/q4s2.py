lines = []
with open("q4/in.txt") as f:
    lines = []
    for l in f:
        lines.append(l.strip())

def tryGet(y,x,lines):
    if y < 0 or x < 0:
        return None
    try:
        return lines[y][x]
    except:
        return None

    
def checkAdjacent(lines, x, y):
    rolls = []
    rolls.append(tryGet(y, x-1, lines))
    rolls.append(tryGet(y,x+1, lines))
    for i in range(3):
        rolls.append(tryGet(y+1,x-1+i, lines))
        rolls.append(tryGet(y-1,x-1+i, lines))
    return rolls.count("@")

def checkState(lines):
    res = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "@":
                if checkAdjacent(lines, x, y) < 4: 
                    res +=1
                    lines[y] = lines[y][:x] + "." + lines[y][x+1:]
    return res
res = 0
prev = []
while True:
    r = checkState(lines)
    if r == 0:
        break
    res += r


        
print(f"res {res}")