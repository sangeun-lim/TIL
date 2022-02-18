import sys
sys.stdin = open('practice2\input.txt')

# def itoa(s, a):
#     # 음수가 들어왔을 때 
#     if s < 0:
#         s = -s
#         while True:
#             int_x = s % 10 
#             a += chr(int_x + 48)
#             s //= 10
#             if s == 0 :
#                 break
#         a += chr(45)
#         return a[::-1]
#     # 양수가 들어왔을 때
#     else:
#         while True:
#             int_x = s % 10 
#             a += chr(int_x + 48)
#             s //= 10
#             if s == 0 :
#                 break
#     return a[::-1]

def itoa(s,a):
    # 0만 들어왔을 때
    ss = s

    if s == 0 :
        return '0'

    while s != 0 :
        # 음수값이 들어오면
        if s < 0 :
            s = -s
            a += chr(s % 10 + 48)
            s //= 10

        # 양수값이 들어오면
       
        else :
            a += chr(s%10 + 48)
            s //= 10
    
    if ss < 0 :
        return '-' + a[::-1]
    else :
        return a[::-1]


for tc in range(1,7):
    num = int(input())
    str_list = ''
    num_str = itoa(num, str_list)

    print(f'#{tc} {num_str} {type(num_str)}')