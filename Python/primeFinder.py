i=2
num=2
while(i<(num/2+1)):
    if (i>=(num/2)):
        print("prime")
        break
    else:
        if (num%i==0):
            print("not prime")
            break
        i+=1
