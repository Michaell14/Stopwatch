s=input()
p=0
while (len(s)>1):
    c=0
    p+=1
    for i in s:
        c+=int(i)
    s=str(c)
print(p)
