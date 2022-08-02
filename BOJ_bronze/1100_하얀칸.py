res = 0
chess = []
for _ in range(8):
    chess.append(list(map(str,input())))

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if chess[i][j] == 'F':
                res += 1
print(res)
