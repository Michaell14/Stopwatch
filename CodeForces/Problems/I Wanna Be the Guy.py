case=int(input())
lst1=list(map(int,input().split(" ")))
lst2=list(map(int,input().split(" ")))
p=lst1[1:]+lst2[1:]
a=list(set(p))
b=list(range(1,case+1))
if len(a)>=len(b) and lst1[0]+lst2[0]>=len(b):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
