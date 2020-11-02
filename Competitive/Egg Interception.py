case, position=map(int, input().split(" "))
lst=list(map(int, input().split(" ")))

count=0
lst2=lst.copy()
lst2.sort()
while (len(lst2)>0):
    print(position)
    m=min(lst2)
    count+=abs(position-(lst.index(m)+1))
    position=lst.index(m)+1
    lst2.remove(m)
print(count)
