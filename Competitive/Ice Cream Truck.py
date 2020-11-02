lst=list(map(int, input().split(" ")))
single=lst[0]
five=lst[1]
num=lst[2]

count=0
while num>five:
    count+=five
    num-=five
count+=num*single
print(count)
