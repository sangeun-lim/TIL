x = int(input())
while True:
    if x % 10 == 0:
        x //= 10
    else:
        break
res = str(x).count('0')
print(res)

#######################
print(input().strip('0').count('0'))