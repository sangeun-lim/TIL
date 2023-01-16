B = 0
C = 0
for i in input():
    if i == 'B':
        B += 1
    else :
        C += 1
print(B//2 + C//2)
############################################
s = input()
print((s.count('B')//2) + (s.count('C')//2))