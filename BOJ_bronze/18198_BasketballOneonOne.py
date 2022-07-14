x = input()
A=B=0
for i in range(len(x)) :
    if x[i] == 'A':
        A += int(x[i+1])
    elif x[i] == 'B':
        B += int(x[i+1])
    else :
        continue
if A > B :
    print('A')
else :
    print('B')

