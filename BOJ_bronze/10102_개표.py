V = int(input())
A = B = 0
x = input()
for i in x :
    if i == 'A':
        A += 1
    else :
        B += 1

if A == B :
    print('Tie')
elif A > B :
    print('A')
else :
    print('B')