lst=list(map(int, input().split(" ")))
a=lst[0]
b=lst[1]
numB=b-a+1

s=0
for i in range(a, b+1):
   if "7" not in str(i):
       s+=i
       for x in str(i):
           s+=int(x)
print(s)
