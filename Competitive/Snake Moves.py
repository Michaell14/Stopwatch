w, h=map(int, input().split(" "))
x,y = map(int, input().split(" "))
eggs=int(input())
lst=[]

for i in range(eggs):
    lst.append(list(map(int, input().split(" "))))

count=0
while eggs>=0:
    for i in lst:
        print(count)
        if x==i[0] or y==i[1]:
            count+=1
            x,y=i[0], i[1]
            break
        elif (abs(x-i[0])==abs(y-i[1])):
            count+=1
            x,y=i[0],i[1]
            break
        else:
            count+=2
            break
    eggs-=1
print(count)
