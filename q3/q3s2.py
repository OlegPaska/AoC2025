

total = 0
digits = [0] * 12
with open("q3/in.txt") as f:
    for l in f:
        li = list(l.strip())
        digits[0] = max(li[:-11])
        for i in range(1,12):
            o = 11 - i
            digits[i] = max(li[digits.index(digits[i-1])+1:-o])

        jolts = int("".join(digits))
        total += jolts
        print(jolts)

print(f"total jolts : {total}")