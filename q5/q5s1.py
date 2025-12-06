ranges = []
ids = []

with open("q5/in.txt") as f:
    nl = False
    for l in f:
        if l == "\n":
            nl = True
            continue
        if not nl:
            ranges.append(l.strip())
        else:
            ids.append(l.strip())

res = 0
for id in ids:
    id = int(id)
    for range in ranges:
        r = range.split('-')
        if id >= int(r[0]) and id <= int(r[1]):
            res += 1
            break

print(res)

