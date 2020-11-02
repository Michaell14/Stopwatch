length=int(input())
s=input()
coor=list(map(int, input().split(" ")))

x=0
y=0
for i in s:
    if i=="U":
       y+=1
    elif i=="D":
        y-=1
    elif (i=="R"):
        x+=1
    else:
        x-=1
print(abs(coor[0]-x)+abs(coor[1]-y))
