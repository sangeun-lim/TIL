dict = {
    '-' : 0,
    '\\' : 1,
    '(' : 2,
    '@' : 3,
    '?' : 4,
    '>' : 5,
    '&' : 6,
    '%' : 7,
    '/' : -1
}

while True :
    s = input()
    if s == '#':
        break

    n = len(s)
    ans = 0

    for i in range(n):
        ans += dict[s[i]] * 8 ** (n-1-i)

    print(ans)