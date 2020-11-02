# AAA
# BBB
# CCC
#-------
#BAAC
d=True
while(d):
    for a in range(1,10):
        for b in range(0,10):
            for c in range(0,10):
                sum= (a*100+a*10+a)+(b*100+b*10+b)+(c*100+c*10+c)
                sum=str(sum)
                if (sum[0]==str(b) and sum[1]==str(a) and sum[2]==str(a) and sum[3]==str(c)):
                    print(sum)
                    d=False
                    break
        
