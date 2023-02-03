# 조합 문제
# 바지 3개 상의 2개 안경 2개이면
# (3+1) * (2+1) * (2+1) - 1
# 1씩 더하는것 그 옷의 종류를 입지 않는 경우, -1은 아무것도 입지않은경우

T = int(input())
for tc in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, kind = input().split()
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1

    result = 1
    for c in clothes.values():
        result *= (c+1)
    print(result - 1)