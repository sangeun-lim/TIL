n = int(input())
arr = [0 for _ in range(n+1)]

prime = []
for i in range(2,n+1): # 소수 배열 초기화해주기
    if arr[i]:
        continue
    prime.append(i)
    # j = 2
    # while i * j <= n:
    #     arr[i*j] = 1
    #     j += 1
    for j in range(i*i, n+1, i):
        arr[j] = 1


s = 0
e = 0
cnt = 0

if prime: # 소수가 존재할 때
    total = prime[0]
    while s <= e:
        if total <= n: # 합이 작거나 같을 때
            if total == n:
                cnt += 1
            e += 1
            if e == len(prime): # 배열 인덱스 초과하면 종료
                break
            total += prime[e]
        else: # 합이 클 때
            total -= prime[s]
            s += 1

print(cnt)