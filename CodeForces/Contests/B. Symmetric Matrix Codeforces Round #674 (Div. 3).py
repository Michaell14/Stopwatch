for case in range(int(input())):
    moreCases, squareSize=map(int, input().split(" "))
    if squareSize%2==1:
        print("NO")
        for s in range(moreCases*2):
            input()
        continue
    t=False
    for i in range(moreCases):
        lst=[]
        lst.append(list(map(int, input().split(" ")))[1])
        lst.append(list(map(int, input().split(" ")))[0])
        if lst[0]==lst[1]:
            t=True

    if t:
        print("YES")
    else:
        print("NO")
