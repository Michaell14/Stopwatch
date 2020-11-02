h=2000000
lst=[True]*h
sum=0
for i in range(2, h):
    if lst[i]:
        sum+=i
        for x in range(i*i, h, i):
            lst[x]=False
print(sum)
