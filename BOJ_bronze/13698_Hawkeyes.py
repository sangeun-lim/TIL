X = input()
lst = [0,1,0,0,2]
for i in X:
    if i == 'A':
        lst[1], lst[2] = lst[2],lst[1]
    elif i == 'B':
        lst[1], lst[3] = lst[3], lst[1]
    elif i == 'C':
        lst[1], lst[4] = lst[4], lst[1]
    elif i == 'D':
        lst[2], lst[3] = lst[3], lst[2]
    elif i == 'E':
        lst[2], lst[4] = lst[4], lst[2]
    else :
        lst[3], lst[4] = lst[4], lst[3]
print(lst.index(1))
print(lst.index(2))

#-----------------------------------------#
change = input()
cup = [1, 0, 0, 2]
case = {'A': [0, 1], 'B': [0, 2], 'C': [0, 3],
        'D': [1, 2], 'E': [1, 3], 'F': [2, 3]}
for c in change:
    cup[case[c][0]], cup[case[c][1]] = cup[case[c][1]], cup[case[c][0]]
print(cup.index(1) + 1)
print(cup.index(2) + 1)