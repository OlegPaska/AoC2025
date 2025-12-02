count = 50
zeros = 0
with open("in.txt") as f:
    for l in f:
        num = int(l[1:])
        isRight = l[0] == "R" 
        if isRight:
            for i in range(num):
                count += 1
                if count % 100 == 0: zeros += 1
        else:
            for i in range(num):
                count -= 1
                if count % 100 == 0: zeros += 1
        

print(zeros)