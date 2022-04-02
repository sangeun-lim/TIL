N = int(input())
cnt = 0
want = N

while True :
    if want < 10 :
        want2 = '0' + str(want)
        want = str(want % 10) + want2[1]
        cnt += 1
    else :
        want2 = want // 10 + want % 10
        want = str(want % 10) + str(want2 % 10)
        cnt += 1

    want = int(want)

    if want == N :
        break

print(cnt)