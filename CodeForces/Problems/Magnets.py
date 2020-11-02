cases=int(input())
lst=[]
count=1
for i in range(cases):
    lst.append(int(input()))

for i in range(len(lst)-1):
    if (lst[i]!=lst[i+1]):
        count+=1
print(count)
