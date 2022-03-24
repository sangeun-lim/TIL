import sys
sys.stdin=open('input.txt')

code = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}

T = int(input())
for tc in range(1,T+1):
    r,c = map(int,input().split())  # 가로 r , 세로 c
    arr = [list(map(int,input())) for _ in range(r)]
    lst = []

    # 1이 들어있는 행 하나만 새로운 리스트에 추출 및 저장
    for i in range(r):
        if 1 in arr[i] :
            lst.append(arr[i])
            break
    # 암호코드만 남기기
    lst = lst[0]
    while lst[-1] == 0 :
        lst.pop(-1)
    while len(lst) % 56 != 0:
        lst.pop(0)

    code_list = []
    # 7개씩 묶기
    for i in range(0,len(lst),7):
        code_list.append(lst[i:i+7])

    # , 없애고 8개씩 한번에 묶어주기 위해
    new_code_list = []
    for i in range(8):
        new_code = ''
        for j in code_list[i]:
            new_code += str(j)
        new_code_list.append(new_code)

    # 2진코드 10진수로 변환
    ans = []
    for i in new_code_list:
        ans.append(code.get(i))

    # 검증코드
    result = (ans[0] + ans[2] + ans[4] + ans[6]) * 3 + ans[1]+ ans[3] + ans[5] + ans[7]

    if result % 10 == 0 :   # 올바른 암호코드라면
        total = 0
        for i in ans:
            total += int(i)
        print(f'#{tc} {total}')
    else :                  # 올바른 암호코드가 아니라면
        print(f'#{tc} {0}')