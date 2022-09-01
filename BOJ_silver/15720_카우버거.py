B,C,D = map(int,input().split()) # B는 주문한 버거의 개수, C는 사이드 메뉴의 개수 , D는 음료의 개수
x = min(B,C,D)
berger = list(map(int,input().split()))
side = list(map(int,input().split()))
drink = list(map(int,input().split()))
berger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)
sum_berger = sum(berger)
sum_side = sum(side)
sum_drink = sum(drink)
total = sum_berger + sum_side + sum_drink

discount_total = 0
for i in range(x):
    discount_total += (berger[i] + side[i] + drink[i]) * 0.9
discount_total += sum(berger[x::])
discount_total += sum(side[x::])
discount_total += sum(drink[x::])

print(total)
print(f'{discount_total:.0f}')