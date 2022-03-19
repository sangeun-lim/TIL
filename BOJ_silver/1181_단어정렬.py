import sys
N = int(input())
word = []
for i in range(N): # 단어 리스트에 입력 받고
    word.append(sys.stdin.readline().strip())
my_set = set(word) # 중복 제거
word = list(my_set) # 다시 리스트에 저장
word.sort() # 알파벳순으로 정렬
word.sort(key=len) # 길이순으로 정렬

for i in word:
    print(i)