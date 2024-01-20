def function(m, n):
    while n != m:
        if n > m:
            n = n - m
        else:
            m = m - n
    return n

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    print(function(m, n))
    
#参考：http://t.csdnimg.cn/wMrnW