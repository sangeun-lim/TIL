M,S,G = map(int,input().split())  # M은 계단수, S는 에스컬레이터 , G는 계단
A,B = map(float,input().split()) # 왼쪽줄 기다리는 시간 A, 오른쪽줄 기다리는 시간 B
L,R = map(int,input().split()) # 왼쪽 L명, 오른쪽 R명

a = (M/G) + (L/A)
b = (M/S) + (R/B)

if a < b :
    print('friskus')
else :
    print('latmask')