lst=[]
for i in range(5):
    lst.append(int(input()))
count=0
for i in range(1,lst[-1]+1):
    for x in lst[:-1]:
        if (i%x==0 and i>=x):
            count+=1
            break
print(count)
