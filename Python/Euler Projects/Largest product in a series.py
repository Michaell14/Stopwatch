def horizontal(matrix):
    prod=0
    for i in range(20):
        for x in range(16):
            p=lst[i][x]*lst[i][x+1]*lst[i][x+2]*lst[i][x+3]
            if p>prod:
                prod=p
    return prod

def vertical(matrix):
    prod=0
    for i in range(20):
        for x in range(16):
            p=lst[x][i]*lst[x+1][i]*lst[x+2][i]*lst[x+3][i]
            if p>prod:
                prod=p
    return prod

def downright(matrix):
    prod=0
    for i in range(16):
        for x in range(16):
            p=lst[i][x]*lst[i+1][x+1]*lst[i+2][x+2]*lst[i+3][x+3]
            if p>prod:
                prod=p
    return prod

def downleft(matrix):
    prod=0
    for i in range(16):
        for x in range(3,17):
            p=lst[i][x+3]*lst[i+1][x+2]*lst[i+2][x+1]*lst[i+3][x]
            if p>prod:
                prod=p
    return prod

lst=[]
for i in range(20):
    lst.append(list(map(int, input().split(" "))))
h=horizontal(lst)
v=vertical(lst)
l=downleft(lst)
r=downright(lst)
lsta=[h,v,l,r]
print(lsta)
