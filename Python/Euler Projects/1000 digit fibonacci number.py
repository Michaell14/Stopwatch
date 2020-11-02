num1=1
num2=1
count=0
while True:
    count+=1
    temp=num1
    num1+=num2
    num2=temp
    if (len(str(num1))>=1000):
        break
print(count+2)
