lst={}
s=input()
start,j=0,0
m=0
for i in range(len(s)):
    if s[i] in lst:
        #finds position of letter in lst
        start=max(start,lst[s[i]]+1)
    #Updates letter position index
    lst[s[i]]=i
    m=max(m,i-start+1)
print(m)
