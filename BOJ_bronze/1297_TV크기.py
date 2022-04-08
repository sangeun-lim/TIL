D, H, W = map(int,input().split()) # 대각선 길이, 높이비율 , 너비 비율

# 피타고라스 성질 이용하기
D = D**2
x = (H**2) + (W**2)
ans = D/x
ans = ans ** 0.5
# 길이 1당 비율값을 각각의 높이와 너비 비율과 곱한다

a = int(H*ans)
b = int(W*ans)

print(f'{a} {b}')