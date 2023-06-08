import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key= lambda x: (x[1], x[0])) # 미팅이 끝나는 시간순으로 정렬

cnt = 0
end = 0
for i in range(n):
    if end <= arr[i][0]:
        cnt += 1
        end = arr[i][1]

print(cnt)