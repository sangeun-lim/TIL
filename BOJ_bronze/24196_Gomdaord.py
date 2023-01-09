x = input()
res = x[0]
while x:
    try:
        res += x[ord(x[0])-64]
        x = x[ord(x[0])-64:]
    except IndexError:
        break
print(res)

################################

s = list(input())

p = 0
while p < len(s):
    print(s[p], end="")
    p += ord(s[p]) - ord('A') + 1