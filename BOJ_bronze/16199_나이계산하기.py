year, month , day = map(int,input().split())
year2, month2, day2 = map(int,input().split())
a = 0 # 만 나이
b = 1 # 세는 낭
c = 0 # 연 나이

if year == year2 :
    a = 0
    b = 1
    c = 0

elif year < year2 and month > month2 :
    a += year2-year-1
    b += year2-year
    c += year2-year

elif year < year2 and month == month2 and day > day2:
    a += year2-year-1
    b += year2-year
    c += year2-year

elif year < year2 and month == month2 and day <= day2:
    a += year2-year
    b += year2-year
    c += year2-year

elif year < year2 and month < month2 :
    a += year2-year
    b += year2-year
    c += year2-year

print(a)
print(b)
print(c)
