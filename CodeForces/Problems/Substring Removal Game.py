testCases=int(input())
bina=[]
for i in range(testCases):
    bina.append(input())



def solve(num):
    count=0
    lst=[]
    for i in range(len(num)):
        if (num[i]=="1"):
           count+=1
        if (num[i]=="0" or i==len(num)-1):
            lst.append(count)
            count=0
    return lst

def sub(lst, num):
    m=max(lst)
    count=0
    location=lst.index(m)
    for i in range(location):
        if (lst[i]>1):
            count+=lst[i]-1
    num= num[:location+count]+num[location+m+count:]
    return m+count, num

y=True
k=True
for i in bina:
    k=True
    score=0
    if "1" not in i:
        print(0)
        k=False
    if ("0" not in i):
        print(len(bina)+1)
        k=False
    if (k):
        while(len(i)>0):
            if "1" not in i:
                break
            lst=solve(i)
            score1, i=sub(lst, i)
            if y:
                score+=score1
                y=False
            else:
                y=True
                pass
        print(score)
        print(lst)
 








        
        
