case=int(input())
lst=[]
for i in range(case):
    input()
    lst.append(list(map(int, input().split(" "))))
    
f=1
for x in lst:
    count=0
    for i in range(len(x)-1):
        if i==0:
            if (x[i]>x[i+1]):
                count+=1
        elif i==len(x)-2:
            if (x[-1]>max(x[:-1])):
                count+=1
        else:
            if (x[i]>max(x[:i]) and x[i] > x[i+1]):
                count+=1
    print("Case #"+str(f)+":",count)
    f+=1
