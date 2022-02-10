import sys
sys.stdin = open('sample_input.txt')

T = int(input())                          # 테스트 케이스 수

for i in range(1, T+1):
    n = int(input())                      # 카드 장수
    card = input()                        # 적힌 숫자

    cards = [0 for i in range(10)]        # 카드의 개수를 세기 위해 값 0이 10개인 배열

    for j in range(n):
        cards[int(card[j])] += 1          # 카드가 나올때 마다 그 개수 증가

    card_cnt = 0                          # 가장 많이 나온 카드의 개수
    for j in range(len(cards)):
        if card_cnt < cards[j]:
            card_cnt = cards[j]

    card_max = 0                          # 많이 나온 카드 중 가장 큰 값을 저장하기 위한 변수수

    for k in range(10):
        if cards[k] == card_cnt :         # 카드의 개수가 같다면
            card_max = k

    print(f'#{i} {card_max} {card_cnt}')
