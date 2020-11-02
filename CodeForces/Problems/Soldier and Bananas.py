cost, mon, numB = map(int, input().split(" "))
c=0
for i in range(numB):
   c+=cost*(i+1)

print(max(0,c-mon))
