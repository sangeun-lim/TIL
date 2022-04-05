T = int(input()) # 테스트 케이스 수
for tc in range(T):
    N, M = map(int,input().split()) # N 은 문서의 개수, M 은 몇번째로 인쇄되었는지 궁금한 문서가 현재 큐에서 몇번째에 놓여있는지를 나타내는 정수
    arr = list(map(int,input().split()))
    cnt = 0
    question = [0 for i in range(N)]
    question[M] = 1

    while True:
        if arr[0] == max(arr): # 문서의 첫번째값이 가장 큰 중요도인가?
            cnt += 1            # 횟수 증가
            if question[0] == 1 : # 인쇄되는 문서가 내가 궁금한 문서의 위치와 같다면
                print(cnt)
                break
            else :              # 그렇지 않다면
                arr.pop(0)      # 맨앞 문서 제거
                question.pop(0) # 위치값도 제거

        else :                  # 가장 큰 중요도가 아니라면
            arr.append(arr.pop(0)) # 문서의 뒤로 보내기
            question.append(question.pop(0)) # 위치값도 뒤로 보내기

