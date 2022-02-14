N = int(input()) # 주어지는 수의 개수
prime = map(int,input().split()) # 주어지는 수

cnt = 0  # 소수의 개수를 셈

for i in prime:
    sosu = 0
    if i > 1 :
        for j in range(2,i): # 2부터 i-1 까지
            if i % j == 0:
                sosu += 1 # 나머지가 0 이면 sosu 증가 <== 소수가 아니라는 뜻
        if sosu == 0:
            cnt += 1 # sosu가 0 이면 소수
print(cnt)
