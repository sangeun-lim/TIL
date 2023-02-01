K = int(input()) # 게임시작할때 폭탄을 들고있는 사람의 번호
N = int(input()) # 질문의 개수
bomb = 210 # 폭탄이 터지는 시간
cnt = 0 # 게임이 흐른 시간
for i in range(N):
    time, Z = map(str,input().split())
    if bomb < cnt :
        print(K)
        break
    else:
        if Z == 'T':
            cnt += int(time)
            if bomb < cnt:
                print(K)
                break
            K = (K+1) % 8
            if K == 0:
                K = 8
        else:
            cnt += int(time)
else:
    print(K)
