n = int(input())

for tc in range(n):
    word = list(input().split())

    res = []

    for i in word:
        res.append(i[::-1])

    for i in res:
        print(i, end=' ')
