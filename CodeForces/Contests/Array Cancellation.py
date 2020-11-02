def isOnlyZero(lst):
    for i in lst:
        if i != 0:
            return True
    return False

case=int(input())
for x in range(case):
    input()
    lst=list(map(int, input().split(" ")))

    score=0
    while isOnlyZero(lst):
        
        for i in range(len(lst)):
            if lst[i]>0:
                f=lst[i+1:]
                forward=[x for x in f if x<0]

                #If there is a negative after the forward
                if len(forward)>0:
                    firstNeg=forward[0]
                    if firstNeg*-1<=lst[i]:
                        lst[i]+=firstNeg
                        ind=f.index(firstNeg)+i+1
                        lst[ind]=0
                        score+=firstNeg*-1
                    else:
                        a=firstNeg
                        firstNeg+=lst[i]
                        ind=f.index(a)+i+1
                        lst[ind]=firstNeg
                        lst[i]=0
                        score+=lst[i]
                    
                else:

                    backwards=[x for x in lst[:i] if x<0]
                    firstNeg=backwards[0]
                    if firstNeg*-1<=lst[i]: 
                        lst[i]+=firstNeg
                        lst[lst.index(firstNeg)]=0
                        score+=firstNeg*-1
                    else:
                        lst[lst.index(firstNeg)]+=lst[i]
                        lst[i]=0
                        score+=lst[i]
               break
    print(score)






                    
