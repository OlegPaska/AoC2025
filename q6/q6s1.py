lines = []

with open("q6/in.txt") as f:
    for l in f:
        lines.append(l[:-1])

operands = []
nums = []
for l in lines:
    if l[0] != "*":
        nums.append([int(x) for x in l.split(' ') if x != ''])
    else:
        operands = ([x for x in l.split(' ') if x != ''])

arranged = []
for j in range(len(nums[0])):
    t = []
    for i in range(len(nums)):
        t.append(nums[i][j])
    arranged.append(t)

res = 0
for i in range(len(operands)):
    if operands[i] == '+':
        res += sum(arranged[i])
    if operands[i] == '*':
        total = 1
        for num in arranged[i]:
            total *= num
        res += total

print(res)

print("hi")

        