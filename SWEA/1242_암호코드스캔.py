import sys

# sys.stdin = open('sample_input.txt')
sys.stdin = open('input.txt')

hexa = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}


T = int(input())
for tc in range(1, T + 1):
    r, c = map(int, input().split())  # 가로 r, 세로 c
    arr = [list(map(str,input())) for _ in range(r)]
    lst = []

    for i in range(r):
        for j in arr[i]:
            if j != '0':            # 0 이 아닌 다른수가 들어있다면
                if arr[i] not in lst: # 중복방지
                    lst.append(arr[i])  # 암호코드 후보 리스트에 추가

    # 리스트에서 ' , ' 제거하고 , 한번에 묶어서 16진수로 표현
    code_list = []
    for i in range(len(lst)):
        new_code =''
        for j in lst[i]:
            new_code += str(j)
        code_list.append(new_code)

    # 16진수에서 2진수로 바꿔주기
    binary_list = []
    for i in code_list:
        binary = ''
        for j in range(len(i)):
            binary += hexa.get(i[j])
        binary_list.append(binary)

    print(f'#{tc} {binary_list}')

    # 1차적으로 뒤에 0 다 제거 및 56개씩 묶어주기
    # 근데 56개 묶고 나서 코드를 구분하는 0이 중간에 있으면 어떻게 처리하지
    # 비율로 판단해야되네..?
    real_binary_list = []
    for i in binary_list:
        a = i.rstrip('0')
        pw = ''
        for j in a[::-1]: # 뒤에서 부터 슬라이싱해서
            pw = j + pw
            if len(pw) == 56 and pw != '0'* 56: # 56개씩 끊기
                real_binary_list.append(pw)
                pw = ''
            # 56개 끊고나서 또 새로운 코드가 나올수도 있으므로 중간에 나오는 0을 다 제거해야됨

    print(real_binary_list)
