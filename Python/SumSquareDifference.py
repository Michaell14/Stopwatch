sumSquare=0
squareSum=0

for i in range(1,101):
    sumSquare+=i*i
for i in range(1,101):
    squareSum+=i
squareSum=squareSum*squareSum
print(squareSum-sumSquare)
