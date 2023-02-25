A,B,C = map(int,input().split())
a = A * B
b = A * C
c = B * C
d = A * B * C
lst = [A,B,C,a,b,c,d]
odd = [] # 홀수
even = [] # 짝수

for i in lst:
    if i % 2:
        odd.append(i)
    else:
        even.append(i)
if len(odd) > 0 :
    print(max(odd))
else:
    print(max(even))
