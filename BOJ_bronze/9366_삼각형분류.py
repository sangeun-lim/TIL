T = int(input())
for tc in range(1,T+1):
    triangle = list(map(int,input().split()))
    triangle.sort()
    A = triangle[0]
    B = triangle[1]
    C = triangle[2]
    print(f'Case #{tc}: ', end='')
    # 삼각형이 되는 경우
    if A + B > C :
        if A == B == C :
            print('equilateral')
        elif A == B or B == C or A == C:
            print('isosceles')
        else:
            print('scalene')
    else:
        print('invalid!')
