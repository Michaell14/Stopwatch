import math
def addprimes(primes):
    i=0
    while i<int(math.sqrt(len(primes))):
        x=i+1
        while x<len(primes):
            if primes[x]%primes[i]==0:
                del primes[x]
                x-=1
            x+=1
        i+=1
    return primes

primes=[x for x in range(2, 1000)]
primes=addprimes(primes)
c=True
num=1
l=False
while True:
    for i in primes:
        if i>=num:
            break
        else:
            if l:
                break
            x=(num-i)//2
            for p in range(0, int(math.sqrt(num))+1):
                if pow(p,p)==x:
                    l=True
                    break
            if not l:
                print(num)
                c=False
                break
    if not c:
        break
    num+=2
