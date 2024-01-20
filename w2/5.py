import math
c = 2
g = c/2

while(abs(g*g-c) > 0.000000001):
    g = (g + c/g)/2

print(g)

c = 2000
g = c/2

while(abs(g*g-c) > 0.000000001):
    g = (g + c/g)/2

print(g)