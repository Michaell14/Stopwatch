testCases=int(input())
case=[]
lst=[]
for i in range(testCases):
    case.append(list(map(int, input().split(" "))))
    lst.append(list(map(int, input().split(" "))))

def fun(i):
    m=max(i)
    i=[(l-m)*-1 for l in i]
    return i

for x,i in zip(case, lst):
    if (len(i)==1):
        print(0)
    else:
        if x[1]%2==0:
            i=fun(i)

        i=fun(i)
 
        print(" ".join([str(k) for k in i]))
