n, m = map(int,input().split())
arr = list(map(int,input().split())) + [0] # runtime error 발생을 막기위해 마지막 리스트에 0 추가(패딩)

s = e = cnt = 0
total = arr[0] # 지금까지의 합
while e < n :
    if total == m:
        cnt += 1
        e += 1
        total += arr[e]
    elif total < m :
        e += 1
        total += arr[e]
    else :
        total -= arr[s]
        s += 1
print(cnt)

#############################
n, m = map(int,input().split())
arr = list(map(int,input().split())) + [0] # runtime error 발생을 막기위해 마지막 리스트에 0 추가(패딩)

s = e = cnt = 0
total = arr[0] # 지금까지의 합
while e < n :
    if total <= m:
        if total == m :
            cnt += 1
        e += 1
        total += arr[e]
    else :
        total -= arr[s]
        s += 1
print(cnt)