case=int(input())
lst=list(map(str,input().split(" ")))
s=""

for i in range(len(lst)):
    if lst[i]=="B":
        for x in range(i+1, len(lst)):
            if lst[x]!="B":
                div=(x-i)%2
                if div==0:
                    if lst[x]=="U":
                        lst[i]="D"
                    else:
                        lst[i]="U"
                else:
                    if lst[x]=="U":
                        lst[i]="U"
                    else:
                        lst[i]="D"


print(" ".join(lst))
                        
        
            
