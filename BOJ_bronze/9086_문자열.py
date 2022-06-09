T = int(input())
for tc in range(T):
    x = input()
    result = []
    result.append(x[0])
    result.append(x[-1])
    print(''.join(result))