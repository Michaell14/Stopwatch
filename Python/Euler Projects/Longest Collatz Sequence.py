

m=0

for n in range(1000000-1,100,-1):
    count=1
    while(n!=1):
        count+=1
        if n%2==0:
            n/=2
        else:
            n=3*n+1
    
    if count>m:
        m=count
print(m)
