for x in range(5):
    n,p=map(str, input().split(" "))

    n=[int(i) for i in list(n)]
    p=int(p)
    dig=n[p]
    for i in range(p):
        n[i]+=dig
    for i in range(p+1, len(n)):
        n[i]=abs(dig-n[i])
    print("".join([str(i) for i in n]))
    
