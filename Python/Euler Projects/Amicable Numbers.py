import math
def find(n):
    for i in range(1, math.floor(int(n/2+1))):
        if n%i==0:
            yield i

lst=[]
count=0
for i in range(1,10000):
    if i not in lst:
        s=sum(find(i))
        ss=sum(find(s))
        
        lst.append(s)
        lst.append(ss)
        if i!=s and i==ss:
            count+=s+ss
print(count)
