s=input()
s=[int(x) for x in (s.split(", ")[2:])]
lst=[]
lst2=[]

lst.append(s[0]-1)
for i in range(len(s)-1):
    lst.append(s[i+1]-s[i]-1)

for i in lst:
    lst2+=[x for x in range(1, i+1)]
print([lst2.count(i) for i in range(1,6)])
