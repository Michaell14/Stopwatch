lst=[]
count=[0]
i=0
while i<len(s)-1:
    if (s[i] not in lst):
        lst.append(s[i])
        c=i
        i+=1
    else:
        count.append(i-sum(count))
        lst.clear()
        i=c+1
        lst.append(s[i])
count.append(len(s)-1-sum(count))
return max(count)
