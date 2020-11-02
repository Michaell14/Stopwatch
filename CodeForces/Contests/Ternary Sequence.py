cases=int(input())
lst=[]
for i in range(cases*2):
    lst.append(list(map(int, input().split(' '))))
x=True
h=True
for i in range(len(lst)-1):
    if x:
        if (lst[i][2]>lst[i+1][2]):
            if (lst[i+1][1]>=lst[i][2]):
                print(2*lst[i][2])
            else:
                print(2*lst[i+1][1])
            h=False
        if (lst[i][2]<lst[i+1][2]):
            if (lst[i+1][2]>=lst[i][1]):
                print(2*lst[i][1])
            else: 
                print(2*lst[i+1][2])
            h=False
            
        if h:
            print(0)

        x=False
    else:
        x=True
        h=True
    
