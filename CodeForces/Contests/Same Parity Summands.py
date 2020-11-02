import math
case=int(input())
for i in range(case):
    total, amount=map(int, input().split(" "))
    div=math.floor(total/amount)
    lst=[]
    for x in range(amount):
        lst.append(div)
    remain=total%amount
    if remain%2==0 and total%2==0:
        print("YES")
        lst[0]+=remain
        print(lst)
    else:
         
        if amount<=(total//2):
            print("YES")
            lst[0]+=remain
            print(lst)
        else:
            print("NO")
