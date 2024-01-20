import math
c = 10
g = c/2

while(abs(g**3-c) > 0.000000001):
    g -= (g**3-c)/(3*c**2)

print(g)