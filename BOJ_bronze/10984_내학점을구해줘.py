T = int(input())
for tc in range(T):
    N = int(input())
    C_total = 0
    G_total = 0
    for n in range(N):
        C ,G = map(float, input().split())
        C_total += C
        G_total += C * G

    if G_total == 0 :
        GPA = 0
    else :
        GPA =  G_total / C_total

    print(f'{int(C_total)} {GPA:.1f}')

