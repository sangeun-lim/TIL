w = int(input())
l = int(input())
h = int(input())

a = min(w,l)
b = max(w,l)

if 2*a >= b and a >= 2 * h:
    print('good')
else:
    print('bad')