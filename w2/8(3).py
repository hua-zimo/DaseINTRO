import math

def dingjifen(n):
    pi = 0
    sum = 0
    for i in range(0, n):
        mid = (i+0.5)/n
        sum += 1/n * math.sqrt(1-mid**2)
    
    pi = sum * 4
    
    return pi

if __name__ == "__main__":
    print(dingjifen(1000))
        
#参考：http://t.csdnimg.cn/vlMKj