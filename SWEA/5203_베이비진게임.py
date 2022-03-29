import sys
sys.stdin = open('sample_input.txt')

def win(player):
    # run 인지 확인
    for i in range(10):
        if player[i] == 3 :
            return True

    # triplet 인지 확인
    for i in range(8):
        if player[i] and player[i+1] and player[i+2]:
            return True

    # 이기지 못함
    return False

T = int(input())
for tc in range(1,T+1):
    card = list(map(int,input().split())) # 카드 입력 받기
    player1 = [0] * 10              # 인덱스가 카드 번호가 되도록 초기화
    player2 = [0] * 10
    res = 0                         # 누가 이겼는지 알려줄 변수

    for i in range(len(card)):
        if not (i % 2) :            # player1부터 나눠주기
            player1[card[i]] += 1
            if win(player1):        # run이나 triplet확인
                res = 1
                break
        else:                       # player2 나눠주기
            player2[card[i]] += 1
            if win(player2):        # run이나 triplet확인
                res = 2
                break

    print(f'#{tc} {res}')