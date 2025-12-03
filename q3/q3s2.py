
def maxi(arr, prev):
    max = [0,0]
    for i in range(prev, len(arr)):
        if int(arr[i]) > int(max[0]):
            max = [arr[i], i+1]
    return max


total = 0
digits = [0] * 12
with open("q3/in.txt") as f:
    for l in f:
        li = list(l.strip())
        digits[0], prev = maxi(li[:-11], 0)
        for i in range(1,12):
            o = 11 - i
            digits[i], prev = maxi(li[:len(li)-o], prev)
            
        jolts = int("".join(digits))
        total += jolts
        print(jolts)

print(f"total jolts : {total}")