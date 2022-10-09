n = int(input())

a = '&ptr;'
print("int a;")
print("int *ptr = &a;")
for i in range(2,n+1):
    print("int " + "*" * i + "ptr" + str(i)+" = " + a)
    a = "&ptr"+str(i)+";"

#####################################3
n = int(input())
value = 'a'
print('int a;')
for i in range(n):
    ast = (i+1) * '*'
    if i == 0:
        target = 'ptr'
    else:
        target = f'ptr{i+1}'
    print(f'int {ast}{target} = &{value};')
    value = target