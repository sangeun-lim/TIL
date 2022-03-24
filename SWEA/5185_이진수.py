import sys
sys.stdin=open('sample_input.txt')

T = int(input())
code = {
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

for tc in range(1,T+1):
    n, m = map(str,input().split())
    ans = ''
    for i in m :
        ans += code.get(i)
    print(f'#{tc} {ans}')

#########################################
code = {
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15
}
T = int(input())
for tc in range(1,T+1):
    n, m = input().split()
    ans = ''

    for i in m[::-1]:
        if i in code :      # A~F값이 들어오면
            i = code[i]     # 숫자로 바꿔주기
        i = int(i)          # str로 들어온 숫자를 int로
        for j in range(4):  # 4자리를 만들어주어야하므로
            ans = str(i%2) + ans
            i //= 2

    print(f'#{tc} {ans}')
