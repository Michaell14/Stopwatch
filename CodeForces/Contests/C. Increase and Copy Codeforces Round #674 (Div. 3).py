import math
for i in range(int(input())):
    m=int(input())
    i=math.ceil(math.sqrt(m))
    print(int(i+(m+i-1)/i-2))
