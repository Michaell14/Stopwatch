input()
lst=list(map(int, input().split(" ")))
count=0
while (lst[0]!=max(lst)):
    count+=1
    ma=lst.index(max(lst))
    if ma!=0:
        lst[ma], lst[ma-1]=lst[ma-1], lst[ma]
for i in range(len(lst)-1,-1,-1):
    if lst[i]==min(lst):
        count+=len(lst)-1-i
        break
print(count)

