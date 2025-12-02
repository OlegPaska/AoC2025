#holy jank. idek i just didnt want to rewrite stuff

def cycleCheck(n):
    num = str(n)
    res = ""
    for i in range(1,len(num)//2+1):
        br = False
        loopingStr = num[:i]
        if len(num) % len(loopingStr) == 0:
            for j in range(len(num)):
                if loopingStr[j%len(loopingStr)] != num[j]:
                    br = True
                    break
        else:
            br = True
        
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