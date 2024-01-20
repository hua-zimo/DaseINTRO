import math

n = float(input())
x = 1
x0 = 1

while True:
    x0 = x
    x = x0 - (x0**3-n)/(3*x**2)   
    if math.fabs(x - x0) < 1e-7:
        break
    
print(x0)

#参考：http://t.csdn.cn/bx3Br