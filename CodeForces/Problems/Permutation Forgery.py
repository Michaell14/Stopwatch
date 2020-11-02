case=int(input())
for i in range(case):
    input()
    lst=list(map(int, input().split(" ")))
    newlst=[]
    newlst=lst[::-1]
    newlst=[str(x) for x in newlst]
    print(" ".join(newlst))
