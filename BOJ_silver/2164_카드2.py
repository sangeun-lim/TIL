from collections import deque

N = int(input())
deque = deque([i for i in range(1,N+1)])

# for i in range(1,N+1):
#     card.append(i)

# while len(card) != 1:
#     card.pop(0)
#     v = card.pop(0)
#     card.append(v)

while len(deque) != 1:
    deque.popleft()
    x = deque.popleft()
    deque.append(x)
print(deque[0])