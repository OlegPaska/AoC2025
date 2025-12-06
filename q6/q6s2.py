lines = []

with open("q6/in.txt") as f:
    for l in f:
        lines.append(l[:-1])

operands = ([x for x in lines[len(lines)-1].split(' ') if x != ''])

res = 0
count = 0
if operands[0] == '+':
    total = 0
else:
    total = 1
for x in range(len(lines[0])):

    num = []
    for y in range(len(lines)-1):
        num.append(lines[y][x])
        
    n = [x for x in num if x != ' ']
    if not n:
        count += 1
        res += total
        print(total)
        total = 0
        if operands[count] == '+':
            total = 0
        else:
            total = 1
        continue
    nn = int("".join(n))
    if operands[count] == '*':
        total *= nn
    elif operands[count] == '+':
        total += nn

print(res + total)