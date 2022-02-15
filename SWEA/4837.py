import sys
sys.stdin = open('sample_input.txt')

T = int(input())                     # 테스트 케이스 개수

for tc in range(1,T+1):

    arr = [1,2,3,4,5,6,7,8,9,10,11,12]                  # 집합 A
    N , K = map(int,input().split())                    # 부분집합 원소의 수 N, 부분집합의 합 K
    cnt = 0

    for i in range(1, 1<<len(arr)):                     # 공집합을 제외한 모든 부분집합의 개수만큼 순회하는 반복
        arr_list = []
        total = 0
        for j in range(len(arr)):                       # 리스트의 요소가 부분집합에 포함되어 있는지 하나하나 확인하기 위한 반복
            if i & (1<<j):                              # i는 부분집합에 들어간 요소 (비트를 비교해서 1이 있느냐 없느냐를 판단)
                                                        # 1이 j만큼씩 이동하면서 i와 비교하여 부분집합에 포함된 요소인지 여부 확인
                arr_list.append(arr[j])
                total += arr[j]
        if len(arr_list) == N and total == K:
            cnt += 1

    print(f'#{tc} {cnt}')