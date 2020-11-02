input()
lst1=list(map(int, input().split(" ")))
lst2=list(map(int, input().split(" ")))

m=0
for i in range(len(lst1)):
    c=0
    for x in range(len(lst1)):
        if lst1[x]==lst2[x]:
            c+=1
    if c>m:
        m=c
    temp=lst2[0]
    for x in range(len(lst2)-1):
        lst2[x]=lst2[x+1]
    lst2[-1]=temp
print(m)
