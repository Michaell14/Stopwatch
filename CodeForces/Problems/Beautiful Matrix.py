

mat=[]
for i in range(5):
    mat.append(list(map(int, input().split(" "))))

for x in mat:
    if 1 in x:
        coo=[mat.index(x)+1, x.index(1)+1]
        break
print(abs(coo[1]-3)+abs(coo[0]-3))
