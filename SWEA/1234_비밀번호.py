import sys
sys.stdin =open('input.txt')

for tc in range(1,11):
    N = list(map(str,input().split()))
    password = list(N[1]) # 비밀번호를 list 형태로 받아주기
    real_password = []

    for p in password:    # 비밀번호를 순차적으로 하나씩 꺼내기
        if real_password and p == real_password[-1]: # 새 리스트가 비어있지 않고, 마지막 값이 p와 같다면
            real_password.pop()                      # 가장 최근에 들어온 값과 짝이 맞으므로 pop
        else :
            real_password.append(p)                  # 새 리스트가 비어있거나, 마지막 값이 p와 같지 않다면 추가

    print(f'#{tc}',''.join(real_password))
