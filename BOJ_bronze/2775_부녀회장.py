T = int(input())

for tc in range(T):
    k = int(input())
    n = int(input())
    floor = [x for x in range(1,n+1)]    # 0층 사는 사람들의 규칙

    for i in range(k):                  # 층 수 만큼 반복
        for j in range(1,n):            # 1 ~ n-1 까지
            floor[j] += floor[j-1]      # 각 층별 각 호실의 사람 수를 규칙에 맞게끔
    print(floor[-1])