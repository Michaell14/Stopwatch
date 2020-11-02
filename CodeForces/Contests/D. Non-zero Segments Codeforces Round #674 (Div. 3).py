case=int(input())
s={0}
cur=0
ans=0
lst=[int(x) for x in input().split(" ")]
for i in range(case):
    cur+=lst[i]
    if cur in s:
        ans+=1
        s={0}
        cur=lst[i]
        
    s.add(cur)

print(ans)
