s=input()
ss=input()
k=""
for i in range(len(s)):
    if (s[i]!=ss[i]):
        k+="1"
    else:
        k+="0"
print(k)
