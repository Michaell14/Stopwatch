friends, height=map(int, input().split(" "))
lst=list(map(int, input().split(" ")))

count=0
for i in lst:
    if i>height:
        count+=1
    count+=1
print(count)
