N = int(input())
arr = []
for tc in range(N):
    a,b,c = map(int,input().split())
    if a == b == c :
        arr.append(10000 + a * 1000)
    elif (a == b and a != c) :
        arr.append(1000 + a * 100)
    elif (a == c and a != b) :
        arr.append(1000 + a * 100)
    elif (b == c and a != b) :
        arr.append(1000 + b * 100)
    else :
        arr.append(max(a,b,c) * 100)
print(max(arr))