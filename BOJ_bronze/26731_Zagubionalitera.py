x = input()
alpha = 'QWERTYUIPASDFGHJKLZXCVBNMO'

for i in alpha:
    if i not in x:
        print(i)
        break