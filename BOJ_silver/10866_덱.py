import sys
N = int(input())
deque = []

for i in range(N):
    order = list(map(str, sys.stdin.readline().split()))

    if order[0] == 'push_front':
        deque.insert(0,order[1])
    elif order[0] == 'push_back':
        deque.append(order[1])
    elif order[0] == 'pop_front':
        if deque:
            v = deque.pop(0)
            print(v)
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if deque:
            v = deque.pop(-1)
            print(v)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(deque))
    elif order[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    else:
        if deque:
            print(deque[-1])
        else:
            print(-1)