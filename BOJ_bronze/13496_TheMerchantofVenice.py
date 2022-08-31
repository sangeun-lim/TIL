K = int(input())
for tc in range(1,K+1):
    # n 은 선박수 , s 는 선박의 속도, d는 계약 만기일까지의 일 수
    n,s,d = map(int,input().split())
    result = 0
    for i in range(n):
        di,vi = map(int,input().split())
        if (d * s >= di):
            result += vi
    print(f'Data Set {tc}:')
    print(result)
    print()