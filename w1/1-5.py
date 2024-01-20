x, y, z = (input().split())

if x >= y :
    if y >= z :
        print(z, y, x)
    else :
        print(y, z, x)
else :
    if z >= y :
        print(x, y, z)
    else :
        if z >= x :
            print(x, z, y)
        else :
            print(z, x, y)
        