total = 0
with open("q3/in.txt") as f:
    for l in f:
        li = list(l.strip())
        fst = max(li[:-1])
        snd = max(li[li.index(fst)+1:])
        jolts = int(fst+snd)
        total += jolts
        print(jolts)

print(f"total jolts : {total}")
