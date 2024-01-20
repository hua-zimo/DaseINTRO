import time

n = int(input())
time_start = time.time() #开始计时

flag = 0
for i in range(2, n):
    if n % i == 0:
        flag = 1
        
time_end = time.time()    #结束计时
time_c= time_end - time_start   #运行所花时间

if flag == 0:
    print(n,"是质数，消耗时间：",time_c,"s")
else:
    print(n,"不是质数，消耗时间：",time_c,"s")