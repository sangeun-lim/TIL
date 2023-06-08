import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for i in range(4)]

for i in range(n):
    a, b, c, d = map(int,input().split())

    arr[0].append(a)
    arr[1].append(b)
    arr[2].append(c)
    arr[3].append(d)

v = [[] for i in range(2)]

for i in range(n):
    for j in range(n):
        v[0].append(arr[0][i] + arr[1][j])
        v[1].append(arr[2][i] + arr[3][j])

v[0].sort()
v[1].sort()

s = 0
e = len(v[1]) - 1
cnt = 0

while s < len(v[0]) and e >= 0:
    # 중복의 경우도 있을 수 있음
    if v[0][s] + v[1][e] == 0:
        temp = v[0][s]
        x = 0
        while s < len(v[0]) and v[0][s] == temp:
            x += 1
            s += 1

        temp = v[1][e]
        y = 0
        while e >= 0 and v[1][e] == temp:
            y += 1
            e -= 1

        cnt += x * y
    elif v[0][s] + v[1][e] > 0:
        e -= 1
    else:
        s += 1
print(cnt)

#-------------------------------#
# 틀림
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = [[] for i in range(4)]
#
# for i in range(n):
#     a, b, c, d = map(int,input().split())
#
#     arr[0].append(a)
#     arr[1].append(b)
#     arr[2].append(c)
#     arr[3].append(d)
#
# v = [[] for i in range(2)]
#
# for i in range(n):
#     for j in range(n):
#         v[0].append(arr[0][i] + arr[1][j])
#         v[1].append(arr[2][i] + arr[3][j])
#
# v[0].sort()
# v[1].sort()
#
# cnt = 0
#
# for i in v[0]:
#     l = 1
#     r = 0
#
#     s = 0
#     e = len(v[1]) - 1
#
#     while s <= e:
#         mid = (s+e) // 2
#
#         if v[1][mid] >= -i:
#             l = mid
#             e = mid - 1
#         else:
#             s = mid + 1
#
#     s = 0
#     e = len(v[1]) - 1
#
#     while s <= e:
#         mid = (s + e) // 2
#
#         if v[1][mid] <= -i:
#             r = mid
#             s = mid + 1
#         else:
#             e = mid - 1
#
#     cnt += r - l + 1
#
# print(cnt)