#ABC = A! + B! + C!
import sys

def factorial(num):
    sum=1
    for x in range(1, num+1):
        sum=sum*x
    return sum
print(sys.version)
f=True
while(f):
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                aa=factorial(a)
                bb=factorial(b)
                cc=factorial(c)
                sum=aa+bb+cc
                sum=str(sum)
                if (len(sum)<3):
                    pass
                elif (sum[0]==str(a) and sum[1]==str(b) and sum[2]==str(c)):
                    print(sum)
                    f=False

                    break
