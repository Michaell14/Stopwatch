nodes, case=map(int, input().split(" "))
lst=list(map(int, input().split(" ")))
for i in range(case):
    start, end=map(int, input().split(" "))
    if start>end:
        start,end=end,start
    forward, backward=0,0
    forward=sum(lst[start-1:end-1])
    backward=sum(lst)-sum(lst[start-1:end-1])
    print(min(forward, backward))
