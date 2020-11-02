numOfLines=int(input())
lst=[]
for i in range(numOfLines):
    lst.append(input())

val=0
for i in lst:
    if "+" in i:
        val+=1
    else:
        val-=1
print(val)
