def pre_order(v):   # 전위 순회
    if v != '.':
        print(v, end='')
        pre_order(ch1[v])
        pre_order(ch2[v])

def in_order(v):    # 중위 순회
    if v != '.':
        in_order(ch1[v])
        print(v, end='')
        in_order(ch2[v])

def post_order(v):  # 후위 순회
    if v != '.':
        post_order(ch1[v])
        post_order(ch2[v])
        print(v, end='')


E = int(input()) # 간선수
tree = [list(map(str,input().split())) for _ in range(E)]
V = E + 1 # 정점수

ch1 = {}
ch2 = {}

for i in range(E):
    ch1[tree[i][0]] = tree[i][1]
    ch2[tree[i][0]] = tree[i][2]

pre_order('A')
print()
in_order('A')
print()
post_order('A')