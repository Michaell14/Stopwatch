first=list(map(int,input().split(" ")))
second=list(map(int,input().split(" ")))

value=second[first[1]-1]
index=second.index(value)
d=True

if (value==0):
    print([i>0 for i in second].count(True))
    d=False
if (d):
    for i in range(index, len(second)):
        if (second[i]<value and second[i]>0):
            print(i)
            d=False
            break
        if (second[i]<=0):
            print(i)
            d=False
            break
if (d):
    print(len(second))
