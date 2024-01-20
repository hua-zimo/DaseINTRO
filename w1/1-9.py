#for循环实现
L = [1, 2, 3, 4, 5]
for i in range(len(L)-1, -1, -1): #从列表最后一个元素开始循环，步长为1
    print(L[i], end = ' ')
#参考：http://t.csdn.cn/FxzDY

#while循环实现

j = len(L) - 1
while j >= 0 :
    print(L[j], end = ' ')
    j -= 1
