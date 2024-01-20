import re

pattern = re.compile(r"(^\d{15}$)|(^\d{17}([0-9]|x)$)")
 
strs = input()
result = pattern.findall(strs)
 
print(result)

#参考：http://t.csdnimg.cn/RL0si