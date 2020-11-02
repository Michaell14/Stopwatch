numStops=int(input())
lst=[]
count=0
h=[]
for i in range(numStops):
    lst.append(list(map(int, input().split(" "))))

for i in lst:
    count-=i[0]
    count+=i[1]
    h.append(count)
print(max(h))
