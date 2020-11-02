f=int(input())
lst=list(map(int, input().split(' ')))
l=list(range(len(lst)))
for i in range(len(lst)):
    l[lst[i]-1]=i+1
l=[str(k) for k in l]
print(' '.join(l))
