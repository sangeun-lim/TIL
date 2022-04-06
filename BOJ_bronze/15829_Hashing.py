a = int(input())
word = input()
total = 0
for i in range(a):
    total += ((ord(word[i])-96) * 31**i )
print(total % 1234567891)