case=int(input())
lst=list(map(int,input().split(' ')))
s=0
for i in range(len(lst)):
    s+=(lst[i]/100)
print(round((100*s/len(lst)),12))
