import sys
sys.stdin=open('sample_input.txt')

def fee(m,e):
    global total

    if e >= total:
        return
    if m > 11:
        total = min(total,e)
        return

    if plan[m] == 0 :
        fee(m+1,e)
    else:
        fee(m+1, e + day * plan[m])
        fee(m+1, e + month)
        fee(m+3, e + three_month)

T = int(input())
for tc in range(1,T+1):
    day, month, three_month, year = map(int,input().split()) # 1일, 1달, 3개월, 1년
    plan = list(map(int,input().split())) # 이용계획

    total = year # 총비용
    fee(0,0)
    print(f'#{tc} {total}')

# ###########################################################
T = int(input())
for tc in range(1,T+1):
    day, month, three_month, year = map(int,input().split()) # 1일, 1달, 3개월, 1년
    plan = [0] + list(map(int,input().split())) # 이용계획
    price =[0 for _ in range(13)]

    for i in range(1,13):
        # 1일 과 1달 비교
        price[i] = min(plan[i] * day, month) + price[i-1]
        # 3개월이상 수영장을 이용할때, 3달간의 가격 비교
        if i > 2 :
            price[i] = min(price[i], three_month + price[i-3])
    # 1년 비교
    result = min(price[12], year)
    print(f'#{tc} {result}')

###########################################################
T = int(input())
for tc in range(1,T+1):
    day, month, three_month, year = map(int,input().split()) # 1일, 1달, 3개월, 1년
    plan = list(map(int,input().split())) # 이용계획
    dp = [0] * 12 # 누적합 중에서 가장 최소값만 누적

    dp[0] = min(day*plan[0], month)                 # 1월까지의 최소값누적
    dp[1] = min(day*plan[1], month) + dp[0]         # 2월까지의 최소값 누적
    dp[2] = min(dp[1] + min(day*plan[2], month), three_month)   # 3월까지의 최소값 누적

    # 4월부터 12월까지의 최소값 누적
    for i in range(3,12):
        # ex) 4월이면 1월 비용 + 3개월치(2~4월) or 3월까지의 누적합 + 4월 1달 가격
        dp[i] = min(dp[i-3] +three_month, dp[i-1] + min(day*plan[i],month))

    result = min(dp[-1],year)
    print(f'#{tc} {result}')
