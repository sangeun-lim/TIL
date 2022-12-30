weight = float(input())
height = float(input())
BMI = weight/(height*height)

if BMI < 18.5 :
    print('Underweight')
elif BMI < 25:
    print('Normal weight')
else:
    print('Overweight')