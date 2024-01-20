n = int(input())

if n < 60:
    print("不合格")
elif n >= 60 and n < 75:
    print("合格")
elif n >= 75 and n <90:
    print("良好")
else:
    print("优秀")