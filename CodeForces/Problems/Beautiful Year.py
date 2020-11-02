s=int(input())
s+=1
s=list(str(s))

def c(s):
    for i in s:
        if s.count(i)>1:
            return False
    return True
count=0
while c(s)!=True:
    s=int(''.join(s))
    s+=1
    s=list(str(s))
print("".join(s))
