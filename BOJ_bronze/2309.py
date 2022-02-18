arr = [int(input()) for _ in range(9)]      # 9명의 키 입력받기
total = sum(arr)                            # 9명의 키의 합

# 키 순으로 정렬
arr.sort()

# 투포인터로 접근
s = 0
e = 8 # 9 - 1

while s < e :
    # 2명의 합이 30 이라면
    # 남은 7명의 합이 100 이니까
    if arr[s] + arr[e] == total - 100 :
        for i in range(9):
            if i == s or i == e :
                continue
            print(arr[i])
        break
    # 2명의 합이 30보다 크다면 후진
    elif arr[s] + arr[e] > total - 100:
        e -= 1
    # 2명의 합이 30보다 작으면  전진
    else :
        s += 1

