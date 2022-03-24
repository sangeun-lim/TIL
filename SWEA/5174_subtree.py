import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def pre_order(v):   # 전위 순회
    global cnt
    if v:
        cnt += 1
        pre_order(ch1[v])
        pre_order(ch2[v])

for tc in range(1,T+1):
    E, N = map(int,input().split())  # 간선의 개수 E, 루트 N
    tree = list(map(int,input().split())) # 트리

    ch1 = [0] * (E+2) # 왼쪽 자식, 원래 간선의 수는 정점의 수 - 1 인데, 트리의 정점시작번호가 1 이라서 E+2 만큼 리스트의 크기를 지정
    ch2 = [0] * (E+2) # 오른쪽 자식
    cnt = 0

    for i in range(E):
        p, c = tree[i * 2], tree[i * 2 + 1]  # p는 부모, c는 자식
        if ch1[p] == 0:  # 자식정점이 없으면
            ch1[p] = c
        else:
            ch2[p] = c
    pre_order(N)
    print(f'#{tc} {cnt}')