atk1, life1 = map(int,input().split())
atk2, life2 = map(int,input().split())

while not (life1 <= 0 or life2 <= 0):
    life1 -= atk2
    life2 -= atk1
if life1 > 0 and life2 <= 0:
    print('PLAYER A')
elif life1 <= 0 and life2 > 0:
    print('PLAYER B')
elif life1 <= 0 and life2 <= 0:
    print('DRAW')

