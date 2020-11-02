testCases=int(input())
heights=[]
for i in range(testCases):
    input()
    heights.append(list(map(int, input().split(" "))))


for x in heights:
    ans=0
    for i in range(len(x)-1):
        ans+=max(0, x[i]-x[i+1])
    print(ans)
        
