lst=[0,1]
for i in range(2,10):
    x=lst[i-2]+lst[i-1]
    lst.append(x)
print(lst)
