N, M = map(int,input().split())
card = list(map(int,input().split()))
card.sort()
card_sum = 0 # M에 가장 가까운 합

for i in range(N-2):                                # 첫번째 값 : 3개 의 합이니까 N-2번 순회, 인덱스 0 부터 시작 N-3번 인덱스까지만
    for j in range(i+1,N-1):                        # 두번째 값 : 인덱스 1 부터 시작, N-2번 인덱스까지만
        for k in range(j+1,N):                      # 세번째 값 : 인덱스 2 부터 시작, N-1번 인덱스까지만
            if card[i]+card[j]+card[k] > M :        # 세 개의 합이 M 초과이면 if문 그냥 continue
                continue
            else :
                result = card[i]+card[j]+card[k]    # 세 개의 합이 M 이하이면 result에 저장
                if card_sum <= result:              # card_sum 갱신
                    card_sum = result
print(card_sum)

## 브루트포스 알고리즘