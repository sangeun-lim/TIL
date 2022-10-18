N = int(input())
lst = list(map(int,input().split()))
total = 100
result = 0
for i in lst:
    res = total * i * 0.01
    result += res
    print(result)
    total = total - total * i * 0.01

########################################
n=int(input())
p = 0
for x in map(int,input().split()):
    p = 1 - (1 - p) * (1 - x / 100)
    print(f"{p*100:.6f}")