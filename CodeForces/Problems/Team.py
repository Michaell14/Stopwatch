numLines=int(input())
nums=[]
total=0
for i in range(numLines):
    nums+=[[int(x) for x in input().split()]]

counter=0
for x in range(numLines):
    for k in range(3):
        if (nums[x][k]==1):
            counter+=1
            if (counter==2):
                total+=1
    counter=0
print(total)
    
