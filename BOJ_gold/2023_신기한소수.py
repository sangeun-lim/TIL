n = int(input())

def check(n):
    cnt = 0

    if n==1 :
        return False

    for i in range(1,n+1):
        if i * i > n:
            break
        if n % i == 0 :
            cnt += 1

    return n == 0 or cnt == 1

def recur(cur, num):

    # if cur != 0 and not check(num):
    #     return
    if not check(num):
        return

    if cur == n :
        print(num)
        return

    for i in range(1,10):
        recur(cur +1 , 10 * num + i)

recur(0,0)