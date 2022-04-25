x,y,z = map(int,input().split())
A,B,C = map(int,input().split())

if z <= C and y <= B and x <= A :
    print('A')

elif y <= B and z <= C :
    if x/2 <= A :
        print('B')
    else :
        print('C')

elif z <= C :
    if y/2 <= B :
        print('D')
    else:
        print('E')