ranges = []

with open("q5/in.txt") as f:
    nl = False
    for l in f:
        if l == "\n": break
        ranges.append(l.strip())


for i in range(len(ranges)):
    changes = True
    delete = set()
    while changes == True:
        changes = False
        for j in range(len(ranges)):
            if i == j: continue
            r1 = list(map(int, ranges[i].split('-')))
            r2 = list(map(int, ranges[j].split('-')))
            if r2[0] in range(r1[0], r1[1]+1):
                if r2[1] > r1[1]:
                    ranges[i] = f"{r1[0]}-{r2[1]}"
                delete.add(j)
                changes == True
            if r2[1] in range(r1[0], r1[1]+1):
                if r2[0] < r1[0]:
                    ranges[i] = f"{r2[0]}-{r1[1]}"
                delete.add(j)
                changes == True

ranges = [x for x in ranges if x not in delete]

res = 0
for i in ranges:
    r = list(map(int, i.split('-')))
    res += r[1] - r[0]

print(ranges)

print(f"res: {res}")



# print(len(idSet))     