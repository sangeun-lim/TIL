n,m = map(int,input().split())
sol = []

def recur():
    if len(sol) == m :
        print(' '.join(map(str,sol)))
        return

    for i in range(1,n+1):
        sol.append(i)
        recur()
        sol.pop()
recur()