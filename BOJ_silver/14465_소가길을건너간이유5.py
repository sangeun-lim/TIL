# 슬라이딩 윈도우
n, k, b = map(int,input().split())
arr = [0 for i in range(n+1)]
for i in range(b):
    arr[int(input())] = 1

result = 0 # 고쳐야하는 신호등 개수
s = 1
e = k
for i in range(s, e+1):
    if arr[i]:
        result += 1

cnt = result
while e < n:
    cnt -= arr[s]
    s += 1
    e += 1
    cnt += arr[e]
    result = min(cnt,result)

print(result)

#-------------------------------------#
#누적합
n, k, b = map(int,input().split())
arr = [0 for i in range(n+1)]
for i in range(b):
    arr[int(input())] = 1

for i in range(n):
    arr[i+1] += arr[i]

result = b
for i in range(k,n+1):
    result = min(result, arr[i] - arr[i-k])
print(result)
