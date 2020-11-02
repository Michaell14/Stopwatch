case=int(input())
lst=[]
for i in range(case):
    lst.append(list(map(int, input().split(' '))))


for i in lst:
    if (i[1]<i[0]):
        if ((i[1]%2==0 and i[0]%2==0) or (i[1]%2==1 and i[0]%2==1)):
            print(0)
        else:
            print(1)
    else:
        print(abs(i[0]-i[1]))
