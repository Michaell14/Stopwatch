case=int(input())
lst=[]
for i in range(case):
    i=input()
    l=[]
    for x in range(len(i)):
        if i[x]!="0":
            l.append(i[x]+((len(i[x:])-1)*"0"))
    print(len(l))
    print(" ".join(l))
