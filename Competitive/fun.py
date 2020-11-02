c, q=map(int, input().split(" "))
p=[0]*c
m=list(map(int, input().split(" ")))
for i in range(q):
    l=list(map(str, input().split(" ")))
    s=l[0]
    a=[int(x) for x in l[1:]]
    f=a[0]-1
    if s=="FILL":
        p[f]=m[f]
    elif s=="POUR":
        g=a[1]-1
        while p[f]>0 and p[g]<m[g]:
            p[f]-=1
            p[g]+=1
    else:
        p[f]=0
p=[str(o) for o in p]
print(*p)
