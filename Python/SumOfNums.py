#Summation of primes
import math
#sum=0
#nums=list(range(2000000))
#nums.remove(1)
#nums.remove(0)

#for i in nums:
#    for x in nums:
#        if x%i==0:
#            nums.remove(x)
#    sum+=i
#print(sum)

sum=0
num=2000000
count=0

array=[]
for x in range(2, num):
    array.append(True)

newArray=list(range(2,math.ceil(math.sqrt(num))))
newnewArray=[]

for i in newArray:
    if (array[i]):
        while i*i+count*i<num:
            array[i*i+count*i]=False
            count+=1

for k in range(2, len(array)):
    if (array[k]):
        sum+=k
print(sum)
            
