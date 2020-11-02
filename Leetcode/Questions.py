s=input()
n=len(s)
m=0
i,j=0,0
while(i<n and j<n):
    if s[j] not in s[i:j]:
        j+=1
    else:
        m=max(m, j-i)
        i+=1
m=max(m,j-i)
print(m)
