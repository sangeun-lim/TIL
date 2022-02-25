import sys
sys.stdin = open('input.txt')

for tc in range(10):
    n = input()
    input_password = list(map(int,input().split()))

    while input_password[-1] > 0:						# 비밀번호에 저장된 값의 마지막 숫자가 0보다 클때동안
        for i in range(1,6):							# 5번이 한 사이클 이므로
            input_password[0] -= i						# 비밀번호리스트의 첫번째 값을 i만큼감소
            input_password.append(input_password.pop(0)) # 감소한 값을 맨 뒤로 보내는 작업
            if input_password[-1] <= 0:					# 맨 뒤의 값이 0보다 작거나 같다면
                input_password[-1] = 0					# 맨 뒤의 값을 0으로 고정
                break									# while문 탈출

    # for i in range(len(input_password)):
    #     input_password[i] = str(input_password[i])
    # print(f'#{n}', ' '.join(input_password))

    print(f'#{n}', *input_password)

# ====================================================
for tc in range(10):
    n = input()
    password = list(map(int,input().split()))

    while password[-1] > 0:
        for i in range(1,6):
            v = password.pop(0)
            v -= i
            if v < 1:
                v = 0
                password.append(v)
                break
            else:
                password.append(v)
    print(f'#{n}', *password)