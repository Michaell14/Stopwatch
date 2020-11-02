
num=100000000
count=0
def divisible(num, count):
    for i in range(1,num+1):
        if num%i==0:
            count+=1
        if count>500:
            break
    return count
while True:
    count=0
    s=sum(list(range(1, num+1)))
    count=divisible(s, count)
    if count>500:
        break
    num+=1
print(sum(list(range(1, num+1))))
