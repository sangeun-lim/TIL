x = input()
y = input()

x_second = int(x[:2]) * 3600 + int(x[3:5]) * 60 + int(x[6:])
y_second = int(y[:2]) * 3600 + int(y[3:5]) * 60 + int(y[6:])

if x_second >= y_second :
    y_second += 86400

time = y_second - x_second
hh = time // 3600
if hh < 10 :
    hh = '0' + str(hh)
mm = time % 3600 // 60
if mm < 10 :
    mm = '0' + str(mm)
ss = time % 3600 % 60
if ss < 10 :
    ss = '0' + str(ss)
print(f'{hh}:{mm}:{ss}')

