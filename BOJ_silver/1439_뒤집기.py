S = input()
cnt0 = 0
cnt1 = 0

str = S[0]

for i in range(1,len(S)):
    if S[i-1] == S[i]:
        str += S[i]
    else:
        if '0' in str:
            cnt0 += 1
        else:
            cnt1 += 1
        str = S[i]

if '0' in str:
    cnt0 += 1
else:
    cnt1 += 1

print(min(cnt0,cnt1))

#-----------------------#
s = input()
cnt = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1
print((cnt+1)//2)