from collections import deque

queue = deque([i for i in range(1,int(input())+1)])
while queue:
    x = queue.popleft()
    print(x, end= ' ')
    if len(queue):
        queue.append(queue.popleft())
    else:
        break
