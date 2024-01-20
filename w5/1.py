n = int(input())

flag = 0
for i in range(2, n):
    if n % i == 0:
        flag = 1

if flag == 0:
    print(n,"是质数")
else:
    print(n,"不是质数")