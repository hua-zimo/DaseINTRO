import math
c = 2
g = c

while(abs(g*g-c) > 0.000000001):
    g = (g + c/g)/2

print(g)

c = 2
g = c/4

while(abs(g*g-c) > 0.000000001):
    g = (g + c/g)/2

print(g)

#改变g与c的关系对结果几乎没有影响。其中，改为g=c结果不变，改为g=c/4结果略大一点。