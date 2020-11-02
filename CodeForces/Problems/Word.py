s=input()
a=sum(1 for i in s if i.islower())
b=len(s)-a
if (a >= b):
    print(s.lower())
else:
    print(s.upper())
