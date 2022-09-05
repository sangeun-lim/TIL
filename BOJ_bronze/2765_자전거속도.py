n = 1
while True:
    x, y ,z = map(float,input().split())
    if y == 0 :
        break
    else :
        distance = (x * 3.1415927 * y) / (5280 * 12)
        z = 3600 / z
        MPH = distance * z
        print(f'Trip #{n}: {distance:.2f} {MPH:.2f}')
        n += 1
