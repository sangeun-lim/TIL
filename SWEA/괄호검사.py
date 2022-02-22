import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    test = input()
    gwalho = []

    blank = 0

    for t in test :
        if t == '(' or t == '{' :
            gwalho.append(t)
        if t == ')':
            if gwalho:                       # 리스트가 비어있지 않을 때,
                if gwalho[-1] == '(':       # 마지막값이 짝이 맞는다면
                    gwalho.pop()
                else :                       # 리스트가 비어있거나, 마지막 값이 짝이 맞지 않는다면
                    break
            else:                               # 리스트가 비어있을때
                blank = 1
                break
        elif t == '}':
            if gwalho:                       # 리스트가 비어있지 않을 때,
                if gwalho[-1] == '{':        # 마지막값이 짝이 맞는다면
                    gwalho.pop()
                else :                       # 리스트가 비어있거나, 마지막 값이 짝이 맞지 않는다면
                    break
            else:                            # 리스트가 비어있을때
                blank = 1
                break

    if gwalho :                              # 최종 리스트가 비어있지 않다면
        print(f'#{tc} {0}')                 # 정상적으로 짝을 이루지 않음
    else :                                   # 최종 리스트가 비어있는데  <==== 시작이 '}' 또는 ')' 인 경우는 append를 안했기 때문에 이 경우도 생각해야함
        if blank == 1:                       # 시작이 } 이나 , ) 인 경우
            print(f'#{tc} {0}')             # 정상적으로 짝을 이루지 않음
        else :                               # 그렇지 않은 경우
            print(f'#{tc} {1}')             # 정상적으로 짝을 이룸


###########################################################

