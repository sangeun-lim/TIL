n,m = map(int,input().split())

def recur(cur):
    if len(cur) == m :
        print(' '.join(map(str, cur)))
        return

    for i in range(1, n+1):
        if i in cur:
            continue
        recur(cur + [i])

recur([])

#########################################
n,m = map(int,input().split())
sol = []

def recur(cur):
    if cur == m :
        for i in sol:
            print(i, end=' ')
        print()
        return
    for i in range(1,n+1):
        if i not in sol:
            sol.append(i)
            recur(cur+1)
            sol.pop()
recur(0)

###########################################
n, m = map(int, input().split())
visited = [False] * (n+1)
s = []

def DFS():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        DFS()
        s.pop()
        visited[i] = False

DFS()