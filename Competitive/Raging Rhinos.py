def iter(lst):
    for i in range(len(lst)-1):
        if lst[i][1]!=lst[i+1][1]:
            return True
    return False
case=int(input())
lst=[]
for i in range(case):
    lst.append(list(map(int, input().split(" "))))

while iter(lst):
    for i in range(len(lst)-1):
        if lst[i][1]==1 and lst[i+1][1]==0:
            if lst[i][0]>lst[1+i][0]:
                lst[i][0]-=lst[i+1][0]
                lst.remove(lst[i+1])
            else:
                lst[i+1][0]-=lst[i][0]
                lst.remove(lst[i])
            break
print(len(lst))
for i in lst:
    i=[str(x) for x in i]
    print(" ".join(i))
