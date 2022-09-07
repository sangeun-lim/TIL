def solution(new_id):
    answer = ''
    # 1. 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2. 알파벳 소문자, 숫자, (-), (_), (.)을 제외한 모든 문자 제거
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word

    # 3. (.)가 2번 연속된 부분을 하나의 (.)로 치환
    while '..' in answer:
        answer = answer.replace("..", ".")

    # 4. (.)가 처음이나 끝에 위치한다면 제거
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    # else :
    #     answer = answer

    if answer[-1] == '.':
        answer = answer[:-1]
    # else :
    #     answer = answer

    # 5. new_id 가 빈문자열 이라면, new_id 는 'a' 대입
    if not answer:
        answer = 'a'
    else :
        answer = answer

    # 6. 글자가 16자 이상이면, 첫 15개를 제외하고 나머지 문자 모두 제거
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]

    # 7. 글자의 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될때까지 반복해서 끝에 붙임
    while len(answer) < 3 :
        answer += answer[-1]
    return answer


############################################################################################
# 다른사람 풀이

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st