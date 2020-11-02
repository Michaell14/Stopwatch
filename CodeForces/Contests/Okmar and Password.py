testCases=int(input())
lst=[]
for i in range(testCases):
    n=int(input())
    lst.append(list(map(str, input().split(" "))))

for i in lst:
    if (i.count(max(i))==len(i)):
        print(len(i))
    else:
        #while(i.count(max(i))!=len(i)):   
        #    s=i[1]+i[0]
        #    del i[:2]
        #    i.append(s)
        print(1)
