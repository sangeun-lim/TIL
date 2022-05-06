x = bin(int(input()))[2:]
cnt = 0
for i in range(len(x)):
    if x[i] == '1' :
        cnt+=1
print(cnt)

################
print(bin(int(input())).count("1"))