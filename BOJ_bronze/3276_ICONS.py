n = int(input())
if n < 4 :
    print(f'{1} {n}')
elif n < 7 :
    print(f'{2} {3}')
elif n < 10 :
    print(f'{3} {3}')
elif n < 13 :
    print(f'{3} {4}')
elif n < 17 :
    print(f'{4} {4}')
elif n < 21 :
    print(f'{4} {5}')
elif n < 26 :
    print(f'{5} {5}')
elif n < 31 :
    print(f'{5} {6}')
elif n < 37 :
    print(f'{6} {6}')
elif n < 43 :
    print(f'{6} {7}')
elif n < 50:
    print(f'{7} {7}')
elif n < 57 :
    print(f'{7} {8}')
elif n < 65 :
    print(f'{8} {8}')
elif n < 73 :
    print(f'{8} {9}')
elif n < 82 :
    print(f'{9} {9}')
elif n < 91 :
    print(f'{9} {10}')
elif n < 101:
    print(f'{10} {10}')

#####################################

n = int(input())
a, b = 0, 0
while a * b < n :
    a += 1
    if a * b >= n :
        break
    b += 1
print(a,b)