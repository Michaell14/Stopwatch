s=input().lower()
s="".join(s.split(" "))
lst=[]
ms=s.count("m")
s=list(s)
for i in range(ms):
    s.remove("m")
s="".join(s)

a="abcdefghijklmnopqrstuvwxyz"
for i in a:
    lst.append([i,0])

for i in s:
    for x in lst:
        if x[0]==i:
            x[1]+=1
            break
m=0
for i in lst:
    if i[1]>m:
        m=i[1]
print(m+ms)
