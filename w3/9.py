import random
n = int(input())

A = list()
B = list()
for i in range(n):
    A.append(random.randint(1, 100))#生成随机数
    B.append(1)

for i in range(n):
    for j in range(n):
        if j != i:
            B[i] *= A[j]

print(A)
print(B)
    