total=0
for i in range(2,4000000):
    number=str(i)
    tot=0
    for each in number:
        tot+=pow(int(each),5)
    if tot==i:
        total+=tot
print(total)
