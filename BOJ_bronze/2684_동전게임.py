p = int(input())

for i in range(p):
    dic = {'TTT': 0, 'TTH': 0, 'THT': 0, 'THH': 0, 'HTT': 0, 'HTH': 0, 'HHT': 0, 'HHH': 0}
    x = input()
    for j in range(38):
        if x[j:j+3] in dic:
            dic[x[j:j+3]] += 1
    for i in dic.values():
        print(i, end=" ")
    print()