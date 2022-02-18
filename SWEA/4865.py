import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # 테스트 케이스 개수

for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    str_list = []         # str1의 값중 중복없이 담기 위해
    str_dict = {}         # 딕셔너리로 값 비교하기 위해

    for i in str1:
        if i not in str_list:
            str_list.append(i)     # str1의 문자열 중 중복없이 str_list에 담기

    for i in str_list:             # str_list에 있는 문자열을 하나씩 받기
        str_dict[i] = 0            # str_dict의 key 값을 i로 value는 0 으로 초기화
        for j in str2:             # str2에 있는 문자열을 인덱스하나씩 받기
            if i == j :            # str_dict의 key값과 str2의 하나씩 들어오는 인덱스에 해당하는 값이 같다면
                str_dict[i] += 1   # key에 해당하는 value 증가

    maxV = 0
    # 최대값 구하기
    for s in str_dict:
        if str_dict.get(s) > maxV :
            maxV = str_dict.get(s)

    print(f'#{tc} {maxV}')

