count = 50
zeros = 0
with open("in.txt") as f:
    for l in f:
        num = int(l[1:])
        count += num  if l[0] == "R" else  -1 * num
        if count != count % 100 or count == 0:
            if count < 0: zeros += 1
            zeros += (abs(count) - (abs(count) % 100))/100
        print(f"zeros: {zeros}")

        #zeros += (abs(count) - (count % 100))/100 if count != count %100 else 0
        count = count % 100
        #if count == 0: zeros += 1
        print(count)
        
print(f"zeros: {zeros}")