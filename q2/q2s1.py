def cycleCheck(n):
    num = str(n)
    res = ""
    for i in range(1,len(num)//2+1):
        br = False
        loopingStr = num[:i]
        for j in range(len(num)):
            if loopingStr[j%len(loopingStr)] != num[j]:
                br = True
                break
        
        if not br: res = num; break
    return res

with open("in.txt") as f:
    res = []
    line = f.readline()
    ranges = line.split(',')
    for fr in ranges:
        r = fr.split('-')
        for i in range(int(r[0]), int(r[1])+1):
            cc = cycleCheck(i)
            if cc: res.append(int(cc))
            
print(f"res: {res}")
print(f"sum {sum(res)}")