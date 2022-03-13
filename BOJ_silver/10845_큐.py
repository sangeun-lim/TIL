import sys

N = int(input())
queue = []

for i in range(N):
    order = list(map(str,sys.stdin.readline().split()))

    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        if not queue:           # 비어있으면
            print(-1)
        else :                  # 비어있지 않으면
            print(queue.pop(0))
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if queue:               # 비어있지 않으면
            print(0)
        else :                  # 비어있으면
            print(1)
    elif order[0] == 'front':
        if not queue:           # 비어있으면
            print(-1)
        else :                  # 비어있지 않으면
            print(queue[0])
    else :
        if not queue :          # 비어있으면
            print(-1)
        else:
            print(queue[-1])