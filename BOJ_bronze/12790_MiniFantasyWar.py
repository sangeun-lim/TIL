T = int(input())
total = 0
for i in range(T):
    a, b, c, d, e, f, g, h = map(int, input().split())
    x = a + e
    y = b + f
    z = c + g
    if x <= 1:
        x = 1
    if y <= 1:
        y = 1
    if z <= 0:
        z = 0
    total = x + 5 * y + 2 * z + 2 * (d+h)
    print(total)