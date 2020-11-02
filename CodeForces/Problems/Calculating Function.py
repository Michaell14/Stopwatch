import math
d=int(input())
if d%2==0:
    print(int(d/2))
else:
    print(int(math.ceil(d/2)*-1))
