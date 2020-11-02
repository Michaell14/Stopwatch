x=int(input())
if x>=0:
    k=list(str(x))
    k.reverse()
    k=int("".join(k))
    if (k<pow(2,31)-1):
        print(k)
    else:
        print(0)
else:
    s=list(str(x))
    s.reverse()
    s=int("".join(s[:-1]))
    if (s<pow(-2,31)):
        print("-"+str(s))
    else:
        print(0)
            
        
