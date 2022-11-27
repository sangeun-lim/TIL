n = int(input())
left = 0
right = 0
for i in range(n):
    x ,y = map(int,input().split())
    if x > y :
        left += x
        left += y
    elif x < y :
        right += x
        right += y
    else :
        left += x
        right += y
print(left,right)