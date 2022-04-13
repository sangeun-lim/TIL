# 1. Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        num = int(input())
        value = factorial(num)
        print("#%d %d! = %d" % (test_case, num, value))


if __name__ == "__main__":
    main()

# 2. Insertion Sort
arr = []
num = 0


def insertionSort():
    global arr
    for i in range(1, num):
        temp = arr[i]
        j = i - 1

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = temp


def printResult():
    for i in range(0, num):
        print(arr[i], end=' ')


def main():
    global arr, num
    T = int(input())

    for test_case in range(1, T + 1):
        num = int(input())
        arr = [int(x) for x in input().split()]

        insertionSort()
        print("#%d" % test_case, end=' ')
        printResult()


if __name__ == "__main__":
    main()

# 3. Quick Sort

arr = []
num = 0


def quick_sort(first, last):
    if first < last:
        pivot = first
        i = first
        j = last

        while i < j:
            while arr[i] <= arr[pivot] and i < last:
                i += 1
            while arr[j] > arr[pivot]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[pivot], arr[j] = arr[j], arr[pivot]

        quick_sort(first, j - 1)
        quick_sort(j + 1, last)


def main():
    global arr, num
    T = int(input())

    for test_case in range(1, T + 1):
        num = int(input())
        arr = [int(x) for x in input().split()]

        quick_sort(0, num - 1)
        print("#%d" % test_case, end=' ')
        for j in range(0, num):
            print(arr[j], end=' ')
        print()


if __name__ == "__main__":
    main()

# 4. Counting Sort
MAX_N = 100
MAX_DIGIT = 10

N = 0
arr = []
cnt = []
sortedArr = []


def calculateDigitNumber():
    global cnt
    for i in range(N):
        cnt[arr[i]] += 1

    for i in range(1, MAX_DIGIT + 1):
        cnt[i] = cnt[i - 1] + cnt[i]


def executeCountingSort():
    global cnt, sortedArr
    for i in range(N - 1, -1, -1):
        sortedArr[cnt[arr[i]] - 1] = arr[i]
        cnt[arr[i]] = cnt[arr[i]] - 1


def main():
    global N, arr, cnt, sortedArr
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        arr = [int(x) for x in input().split()]
        sortedArr = [int(0)] * N
        cnt = [int(0)] * 11

        calculateDigitNumber()
        executeCountingSort()

        print("#%d" % test_case, end=' ')
        for i in range(N):
            print("%d" % sortedArr[i], end=' ')

        print()


if __name__ == "__main__":
    main()

# 5. Binary Search
def binarySearch(arr, low, high, target):
    if low > high:
        print("-1", end=' ')
        return

    mid = (low + high) // 2

    if target < arr[mid]:
        binarySearch(arr, low, mid - 1, target)
    elif arr[mid] < target:
        binarySearch(arr, mid + 1, high, target)
    else:
        print(mid, end=' ')
        return


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        print("#%d" % test_case, end=' ')
        M = int(input())
        N = int(input())

        arr = list(map(int, input().split()))
        targetvalue = list(map(int, input().split()))

        for idx in range(N):
            binarySearch(arr, 0, M - 1, targetvalue[idx])
        print()


if __name__ == "__main__":
    main()

# 6. DFS Searching
def depthFirstSearch(v, depth):
    global maxEdge

    if v == end:
        if maxEdge < 0 or depth < maxEdge:
            maxEdge = depth
        return

    visit[v] = True

    for i in range(1, vertex + 1):
        if MAP[v][i] == 1 and visit[i] is False:
            depthFirstSearch(i, depth + 1)
            visit[i] = False


def main():
    global vertex, end, visit, MAP, maxEdge

    T = int(input())

    for test_case in range(1, T + 1):
        vertex, edge, start, end = map(int, input().split())
        MAP = [[0] * (vertex + 1) for _ in range(vertex + 1)]
        visit = [False] * (vertex + 1)
        for _ in range(edge):
            v1, v2 = map(int, input().split())
            MAP[v1][v2] = 1
        maxEdge = -1
        depthFirstSearch(start, 0)
        print("#%d %d" % (test_case, maxEdge))


if __name__ == "__main__":
    main()

# 7. BFS Searching
class Queue:
    class Point:
        def __init__(self, y, x, c):
            self.y = y
            self.x = x
            self.c = c

    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.head = self.rear = 0

    def isEmpty(self):
        return self.head <= self.rear

    def enQueue(self, y, x, c):
        self.queue[self.head] = self.Point(y, x, c)
        self.head = self.head + 1

    def deQueue(self):
        if self.isEmpty():
            return None
        self.rear = self.rear + 1
        return self.queue[self.rear - 1]


def breadthFirstSearch():
    queue = Queue(row * column)
    queue.enQueue(0, 0, 0)
    MAP[0][0] = 0

    while queue.isEmpty() == False:
        p = queue.deQueue()

        if p.y == row - 1 and p.x == column - 1:
            return p.c

        if p.y + 1 < row and MAP[p.y + 1][p.x]:
            queue.enQueue(p.y + 1, p.x, p.c + 1)
            MAP[p.y + 1][p.x] = 0
        if p.x + 1 < column and MAP[p.y][p.x + 1]:
            queue.enQueue(p.y, p.x + 1, p.c + 1)
            MAP[p.y][p.x + 1] = 0
        if p.y - 1 >= 0 and MAP[p.y - 1][p.x] != 0:
            queue.enQueue(p.y - 1, p.x, p.c + 1)
            MAP[p.y - 1][p.x] = 0
        if p.x - 1 > 0 and MAP[p.y][p.x - 1] != 0:
            queue.enQueue(p.y, p.x - 1, p.c + 1)
            MAP[p.y][p.x - 1] = 0

    return -1


def main():
    global MAP, row, column
    T = int(input())

    for test_case in range(1, T + 1):
        row, column = map(int, input().split())
        MAP = [[int(num) for num in input().split()] for _ in range(row)]
        print("#%d %d" % (test_case, breadthFirstSearch()))


if __name__ == "__main__":
    main()

# 8. Parametric Search
MAX_RIBBON = 100

K = 0
N = 0
sizeRibbonTape = [None for _ in range(MAX_RIBBON)]


def search(low, high):
    max = -1

    while low <= high:
        mid = low + (high - low) // 2

        numRibbonTape = 0
        for i in range(K):
            numRibbonTape += sizeRibbonTape[i] // mid

        if numRibbonTape >= N:
            low = mid + 1
            if max < mid:
                max = mid
        else:
            high = mid - 1

    return max


def main():
    global K, N

    T = int(input())

    for test_case in range(1, T + 1):
        low, high = 1, 0
        K = int(input())
        N = int(input())

        for i in range(K):
            sizeRibbonTape[i] = int(input())
            if high < sizeRibbonTape[i]:
                high = sizeRibbonTape[i]

        max = search(low, high)

        print("#%d %d" % (test_case, max))


if __name__ == "__main__":
    main()

# 9. DP
N = 0
dp = None
board = None


def findSticker():
    global dp
    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    dp[0][1] = dp[1][0] + board[0][1]
    dp[1][1] = dp[0][0] + board[1][1]

    for i in range(2, N):
        dp[0][i] = max(dp[0][i - 2], dp[1][i - 2])
        dp[0][i] = max(dp[1][i - 1], dp[0][i])
        dp[0][i] += board[0][i]

        dp[1][i] = max(dp[0][i - 2], dp[1][i - 2])
        dp[1][i] = max(dp[0][i - 1], dp[1][i])
        dp[1][i] += board[1][i]


def main():
    global N, board, dp

    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        board = [[int(num) for num in input().split()] for _ in range(2)]
        dp = [[0] * 100001 for _ in range(2)]

        findSticker()

        print("#%d %d" % (test_case, max(dp[0][N - 1], dp[1][N - 1])))


if __name__ == "__main__":
    main()

# 10. Permutation & Combination
combinationStack = []


def printString(cArr):
    for i in cArr:
        print(i, end='')
    print()


def swap(cArr, x, y):
    cArr[x], cArr[y] = cArr[y], cArr[x]


def permutation(cArr, l, r):
    if l == r:
        printString(cArr)
    else:
        for i in range(l, r + 1, 1):
            swap(cArr, l, i)
            permutation(cArr, l + 1, r)
            swap(cArr, l, i)


def push(ch):
    combinationStack.append(ch)


def pop():
    combinationStack.pop()


def combination(cArr, length, offset, k):
    if k == 0:
        printString(combinationStack)
    else:
        for i in range(offset, length - k + 1, 1):
            push(cArr[i])
            combination(cArr, length, i + 1, k - 1)
            pop()


def main():
    global cArr, N, K
    T = int(input())

    for test_case in range(1, T + 1):
        cArr = list(input())

        N = int(input())
        K = int(input())

        print("#%d" % test_case)

        permutation(cArr[0:N], 0, N - 1)
        combination(cArr, N, 0, K)


if __name__ == "__main__":
    main()

# 11. DFS Algorithm
def depthFirstSearch(v, depth):
    global maxEdge

    if v == end:
        if maxEdge < 0 or depth < maxEdge:
            maxEdge = depth
        return

    visit[v] = True

    for i in range(1, vertex + 1):
        if MAP[v][i] == 1 and visit[i] is False:
            depthFirstSearch(i, depth + 1)
            visit[i] = False


def main():
    global vertex, end, visit, MAP, maxEdge

    T = int(input())

    for test_case in range(1, T + 1):
        vertex, edge, start, end = map(int, input().split())
        MAP = [[0] * (vertex + 1) for _ in range(vertex + 1)]
        visit = [False] * (vertex + 1)
        for _ in range(edge):
            v1, v2 = map(int, input().split())
            MAP[v1][v2] = 1
        maxEdge = -1
        depthFirstSearch(start, 0)
        print("#%d %d" % (test_case, maxEdge))


if __name__ == "__main__":
    main()

# 12. BFS Algorithm
class Queue:
    class Point:
        def __init__(self, y, x, c):
            self.y = y
            self.x = x
            self.c = c

    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.head = self.rear = 0

    def isEmpty(self):
        return self.head <= self.rear

    def enQueue(self, y, x, c):
        self.queue[self.head] = self.Point(y, x, c)
        self.head = self.head + 1

    def deQueue(self):
        if self.isEmpty():
            return None
        self.rear = self.rear + 1
        return self.queue[self.rear - 1]


def breadthFirstSearch():
    queue = Queue(row * column)
    queue.enQueue(0, 0, 0)
    MAP[0][0] = 0

    while queue.isEmpty() == False:
        p = queue.deQueue()

        if p.y == row - 1 and p.x == column - 1:
            return p.c

        if p.y + 1 < row and MAP[p.y + 1][p.x]:
            queue.enQueue(p.y + 1, p.x, p.c + 1)
            MAP[p.y + 1][p.x] = 0
        if p.x + 1 < column and MAP[p.y][p.x + 1]:
            queue.enQueue(p.y, p.x + 1, p.c + 1)
            MAP[p.y][p.x + 1] = 0
        if p.y - 1 >= 0 and MAP[p.y - 1][p.x] != 0:
            queue.enQueue(p.y - 1, p.x, p.c + 1)
            MAP[p.y - 1][p.x] = 0
        if p.x - 1 > 0 and MAP[p.y][p.x - 1] != 0:
            queue.enQueue(p.y, p.x - 1, p.c + 1)
            MAP[p.y][p.x - 1] = 0

    return -1


def main():
    global MAP, row, column
    T = int(input())

    for test_case in range(1, T + 1):
        row, column = map(int, input().split())
        MAP = [[int(num) for num in input().split()] for _ in range(row)]
        print("#%d %d" % (test_case, breadthFirstSearch()))


if __name__ == "__main__":
    main()

# 13. Dijkstra
N = 100
INF = 100000
MAP = [[0] * (N + 1) for _ in range(N + 1)]
visit = [False] * (N + 1)
dist = [0] * (N + 1)


def dijkstra():
    global dist, visit, MAP
    v = 0
    dist[start] = 0

    for i in range(1, vertex + 1):
        min = INF
        for j in range(1, vertex + 1):
            if visit[j] == False and min > dist[j]:
                min = dist[j]
                v = j

        visit[v] = True

        for j in range(1, vertex + 1):
            if dist[j] > dist[v] + MAP[v][j]:
                dist[j] = dist[v] + MAP[v][j]


def main():
    global MAP, dist, visit, vertex, start

    T = int(input())

    for test_case in range(1, T + 1):
        vertex, start, end = map(int, input().split())
        edge = int(input())

        for i in range(1, vertex + 1):
            for j in range(1, vertex + 1):
                if i != j:
                    MAP[i][j] = INF

        for i in range(1, edge + 1):
            FROM, TO, value = map(int, input().split())
            MAP[FROM][TO] = value

        for i in range(1, vertex + 1):
            dist[i] = INF
            visit[i] = False

        dijkstra()
        print("#%d %d" % (test_case, dist[end]))


if __name__ == "__main__":
    main()

# 14. Floyd Warshall
INFINITY = 999999


def floyd():
    for k in range(n):
        for i in range(n):
            if k == 0:
                for j in range(n):
                    result[i][j] = weight[i][j]
            for j in range(n):
                if result[i][k] + result[k][j] < result[i][j]:
                    result[i][j] = result[i][k] + result[k][j]


def main():
    global result, weight, n

    T = int(input())

    for test_case in range(1, T + 1):

        n = int(input())
        m = int(input())

        result = [[0] * n for _ in range(n)]
        weight = [[INFINITY] * n for _ in range(n)]
        for i in range(n):
            weight[i][i] = 0

        for _ in range(m):
            st, en, w = map(int, input().split())
            if weight[st - 1][en - 1] > w:
                weight[st - 1][en - 1] = w

        floyd()

        print("#%d" % test_case)
        for i in range(n):
            for j in range(n):
                print(result[i][j], end=' ')
            print()


if __name__ == "__main__":
    main()

# 15. Plane Sweeping
class Rec:
    def __init__(self, x, y1, y2, end):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.end = end


def update(x, left, right, nodeLeft, nodeRight, val):
    global tree
    if left > nodeRight or right < nodeLeft:
        return
    if left <= nodeLeft and right >= nodeRight:
        cnt[x] += val
    else:
        mid = (nodeLeft + nodeRight) >> 1
        update(x * 2, left, right, nodeLeft, mid, val)
        update(x * 2 + 1, left, right, mid + 1, nodeRight, val)

    tree[x] = 0
    if cnt[x] > 0:
        tree[x] = nodeRight - nodeLeft + 1
    if cnt[x] == 0 and nodeLeft < nodeRight:
        tree[x] = tree[x * 2] + tree[x * 2 + 1]


def main():
    global tree, cnt
    T = int(input())

    for test_case in range(1, T + 1):

        N = int(input())

        v = [0] * N * 2

        idx = 0
        for _ in range(N):
            x1, y1, x2, y2 = map(int, input().split())
            v[idx] = Rec(x1, y1, y2, 1)
            idx = idx + 1
            v[idx] = Rec(x2, y1, y2, -1)
            idx = idx + 1

        v = sorted(v, key=lambda rec: rec.x)

        tree = [0] * 65538
        cnt = [0] * 65538
        px = v[0].x
        ans = 0
        for i in range(0, idx):
            ans += (v[i].x - px) * tree[1]
            update(1, v[i].y1, v[i].y2 - 1, 0, 32768, v[i].end)

            px = v[i].x

        print("#%d %d" % (test_case, ans))


if __name__ == "__main__":
    main()

# 16. Minimum Spanning Tree
def minKey(key, mstSet):
    min = 2147483647
    for v in range(0, V):
        if (mstSet[v] == 0) and (key[v] < min):
            min = key[v]
            min_index = v
    return min_index


def printMST(parent):
    weightSum = 0
    for i in range(1, V):
        weightSum += graph[i][parent[i]]
    print(weightSum)


def primMST():
    parent = [0] * 100
    key = [2147483647] * 100
    mstSet = [0] * 100
    key[0] = 0
    parent[0] = -1
    for count in range(0, V - 1):
        u = minKey(key, mstSet)
        mstSet[u] = 1
        for v in range(0, V):
            if graph[u][v] and (mstSet[v] == 0) and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]
    printMST(parent)


def main():
    global graph, V
    T, V = map(int, input().split())
    for test_case in range(1, T + 1):
        graph = [[int(x) for x in input().split()] for y in range(V)]
        print("#%d" % test_case, end=' ')
        primMST()


if __name__ == "__main__":
    main()

# 17. Topological Sort
MAX_N = 25
MAX_M = 25
CONNECTED = 1
NOT_CONNECTED = 0
NOT_UPDATED_YET = 0
NOT_VISITED = -1
DUPLICATE = -2

Map = [[0] * MAX_N for i in range(MAX_N)]
count = [0] * MAX_N
queue = []
stack = []
nodes = []


def mark_duplicate(item):
    for i in range(0, len(stack)):
        if stack[i] == item:
            stack[i] = DUPLICATE


class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None

    def reset(self):
        self.prev = None

    def push(self, other):
        if self.prev == None:
            self.prev = other
            return
        head = self
        while head.prev != None:
            head = head.prev
        head.prev = other


for i in range(0, MAX_N):
    nodes.append(Node(i))


def reset():
    for i in range(0, MAX_N):
        for j in range(0, MAX_N):
            Map[i][j] = 0
    for i in range(0, MAX_N):
        count[i] = 0
    queue.clear()
    stack.clear()
    for i in range(0, MAX_N):
        nodes[i].reset()


def connected(src, dest):
    return Map[src][dest] == CONNECTED


def traverse(idx):
    mark_duplicate(nodes[idx].item)
    stack.append(nodes[idx].item)
    cur = nodes[idx].prev
    while cur != None:
        traverse(cur.item)
        cur = cur.prev


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        n, m = map(int, input().split())
        dest = int(input())
        reset()

        for i in range(0, m):
            s, d = map(int, input().split())
            Map[s - 1][d - 1] = CONNECTED
            count[d - 1] += 1

        for i in range(0, n):
            if count[i] == 0:
                queue.append(i)

        while len(queue) > 0:
            src = queue.pop(0)
            for i in range(0, n):
                if connected(src, i):
                    node = Node(src)
                    nodes[i].push(node)
                    count[i] -= 1
                    if count[i] == 0:
                        queue.append(i)

        print("#%d " % test_case, end='')

        if nodes[dest - 1].prev == None:
            print("Not reached")
        else:
            traverse(dest - 1)
            while len(stack) > 0:
                item = stack.pop()
                if item == DUPLICATE:
                    continue
                print("%d " % (item + 1), end='')
            print()


if __name__ == "__main__":
    main()

# 18. Maximum Flow
MAX_V = 10
INF = 987654321
V = 0


def networkFlow(source, sink):
    flow = [[0] * MAX_V for i in range(MAX_V)]
    parent = [0] * MAX_V
    totalFlow = 0
    while True:
        for p in range(0, V):
            parent[p] = -1
        q = list()
        parent[source] = source
        q.append(source)
        while len(q) > 0:
            here = q[0]
            q.pop(0)
            for there in range(0, V):
                if (capacity[here][there] - flow[here][there] > 0) and (parent[there] == -1):
                    q.append(there)
                    parent[there] = here
        if parent[sink] == -1:
            break
        amount = INF
        p = sink
        while p != source:
            if capacity[parent[p]][p] - flow[parent[p]][p] > amount:
                amount = amount
            else:
                amount = capacity[parent[p]][p] - flow[parent[p]][p]
            p = parent[p]
        p = sink
        while p != source:
            flow[parent[p]][p] += amount
            flow[p][parent[p]] -= amount
            p = parent[p]
        totalFlow += amount
    return totalFlow


def main():
    global V, E, capacity

    T = int(input())
    for test_case in range(1, T + 1):
        V, E = map(int, input().split())
        capacity = [[0] * MAX_V for i in range(MAX_V)]
        for i in range(0, E):
            here, there, C = map(int, input().split())
            capacity[here][there] = C
        answer = networkFlow(0, V - 1)
        print("#%d %d" % (test_case, answer))


if __name__ == "__main__":
    main()

# 19. Bipartite Match
MAX = 1000
matchA = [0] * MAX
matchB = [0] * MAX
adj = [[0] * MAX for i in range(MAX)]
visited = [False] * MAX


def dfs(a):
    if visited[a]:
        return False
    visited[a] = True
    for b in range(0, countB):
        if adj[a][b] != 0 and (matchB[b] == -1 or dfs(matchB[b])):
            matchA[a] = b
            matchB[b] = a
            return True
    return False


def bipartiteMatch():
    size = 0
    for start in range(0, countA):
        for i in range(0, countA):
            visited[i] = False
        if dfs(start):
            size += 1
    return size


def initialize():
    for i in range(0, countA):
        matchA[i] = -1
        for j in range(0, countB):
            adj[i][j] = 0
    for i in range(0, countB):
        matchB[i] = -1


def main():
    global visited, countA, countB
    T = int(input())
    for test_case in range(1, T + 1):
        countA = int(input())
        countB = int(input())
        initialize()
        adjCount = int(input())
        for i in range(0, adjCount):
            a, b = map(int, input().split())
            adj[a - 1][b - 1] = 1
        print("#%d %d" % (test_case, bipartiteMatch()))


if __name__ == "__main__":
    main()