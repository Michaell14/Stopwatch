rooms=int(input())
lst=[]
for i in range(rooms):
    lst.append(list(map(int, input().split(' '))))

count=0
for i in lst:
    if i[0]<=i[1]-2:
        count+=1

print(count)
