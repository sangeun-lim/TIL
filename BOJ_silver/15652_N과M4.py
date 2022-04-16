n,m = map(int,input().split())
sol = []

def recur(cur):
    if len(sol) == m :
        print(' '.join(map(str,sol)))
        return

    for i in range(cur,n+1):
        sol.append(i)
        recur(i)
        sol.pop()
recur(1)
