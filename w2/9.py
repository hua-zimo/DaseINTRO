import numpy as np
import math
import random

def function(x):
    return x**2 + 4*x*math.sin(x)

def montecarlo(n, a, b):
    m = 0
    sum = 0
    y1 = function(a)
    y2 = function(b)
    
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, y2)
        if y <= function(x):
            sum += 1
    
    return (sum/n)*(abs(b-a))*(y2)

if __name__ == "__main__":
    print(montecarlo(1000, 2, 3))

#参考：http://t.csdnimg.cn/nrLFa
