number=2
primenum=0
yes=False
while(primenum<10001):
    
    for i in range(2, number):
        if (number%i==0 and yes==False and number!=i):
            yes=True
            break
    if (yes==False):
        primenum+=1
    number+=1
    yes=False
print(number-1)
