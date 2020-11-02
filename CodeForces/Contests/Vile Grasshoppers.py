p,y =map(int, input().split(" "))
y=list(range(2,y+1))
y=[i for i in y if i not in range(2, p+1)]
c=False
for i in reversed(y):
    if c:
        break
    for x in range(2, i+1):
        if (i%x==0 and x>p):
            print(i)
            c=True
            break
        elif i%x==0:
            break
if not c:
    print(-1)
