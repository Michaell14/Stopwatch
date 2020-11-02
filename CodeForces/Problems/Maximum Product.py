case=int(input())
for i in range(case):
    input()

    nums=list(map(int, input().split(" ")))
    nums.sort()
    
    s1=1
    s2=1
    if len(nums)==5:
        for x in nums:
            s1*=x
    else:
        for x in range(len(nums)-1,len(nums)-6,-1):
            s1*=nums[x]
        for x in range(5):
            s2*=nums[x]
        s1=max(s1,s2)
    print(s1)
