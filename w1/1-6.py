w, x, y, z = (input().split())

a = [w, x, y, z]
a.sort(reverse = True) #排序并进行倒序

print(" ".join(str(i) for i in a)) #输出列表元素，中间空格

#参考：http://t.csdn.cn/FXzP9 http://t.csdn.cn/A9KhK