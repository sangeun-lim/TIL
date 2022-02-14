n = int(input())                # 테스트 횟수

for i in range(n):
    OX = input()                # 들어오는 테스트

    score = 1                   # 맞으면 더해줄 값
    total = 0                   # 총합

    for j in OX:                # input값을 순차적으로 줌
        if j == 'O' :
            total += score      # 'O'가 나오면 계속 연속점수를 줌
            score += 1          # O가 연속으로 나오면 +1 점을 더 주기 위해
        else :                  # j 가 X 값이 들어오면
            score = 1           # 다시 'O'가 오면 1점으로 초기화 하기 위함

    print(total)                # 총점 출력
