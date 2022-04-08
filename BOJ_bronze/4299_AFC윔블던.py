a, b = map(int, input().split())
e = (a + b) // 2
f = a - e
if a < b or (a + b) % 2:
    print(-1)
else:
    print(f'{max(e, f)} {min(e, f)}')

##############

a, b = map(int, input().split())
if a + b < 0 or a - b < 0 or (a + b) % 2:
    print(-1)
else:
    c = (a + b) // 2
    d = a - c
    print(max(c, d), min(c, d))
