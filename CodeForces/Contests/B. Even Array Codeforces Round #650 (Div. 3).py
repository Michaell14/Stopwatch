for _ in range(int(input())):
    d={"even":0, "odd":0}
    input()
    lst=[int(x) for x in input().split(" ")]
    for i in range(len(lst)):
        if i%2!=lst[i]%2:
            if lst[i]%2==0:
                d["even"]+=1
            else:
                d["odd"]+=1
    if d["even"]==d["odd"]:
        print(d["odd"])
    else:
        print(-1)
