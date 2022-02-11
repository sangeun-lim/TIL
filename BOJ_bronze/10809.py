S = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if i in S :
        print(S.find(i), end = ' ')
    else :
        print(-1,  end = ' ')