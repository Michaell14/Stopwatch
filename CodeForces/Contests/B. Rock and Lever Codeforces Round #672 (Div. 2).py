bin(6)[2:].zfill(8)

for i in range(int(input())):
    input()
    lst=[int(x) for x in input().split(" ")]
    c=0
    for x in range(len(lst)-1):
        for xx in range(x+1, len(lst)):
            if lst[x]&lst[xx]>=lst[x]^lst[xx]:
                c+=1
    print(c)
