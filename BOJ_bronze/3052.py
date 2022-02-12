my_lst = []
for i in range(10):
    a = int(input())
    my_lst.append(a)

div_list = []
for i in my_lst:
    b = i % 42
    if b not in div_list:
        div_list.append(b)
    
print(len(div_list))


