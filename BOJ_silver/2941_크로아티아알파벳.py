x = input()
x = x.replace('c=', '+')
x =x.replace('c-','+')
x =x.replace('dz=','+')
x =x.replace('d-','+')
x =x.replace('lj','+')
x =x.replace('nj','+')
x =x.replace('s=','+')
x =x.replace('z=','+')
print(len(x))

#######################################
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croa:
    word = x.replace(i, '+')
print(len(word))