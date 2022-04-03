word = input()
cnt = 0
for i in range(len(word)):
    if word[i] in 'ABC':
       cnt += 3
    elif word[i] in 'DEF':
        cnt += 4
    elif word[i] in 'GHI':
        cnt += 5
    elif word[i] in 'JKL':
        cnt += 6
    elif word[i] in 'MNO':
        cnt += 7
    elif word[i] in 'PQRS':
        cnt += 8
    elif word[i] in 'TUV':
        cnt += 9
    elif word[i] in 'WXYZ':
        cnt += 10

print(cnt)