numOfInputs=int(input())
lst=[]
for i in range(numOfInputs):
    lst.append(input())

for word in lst:
    if (len(word)>10):
        print(word[0]+str(len(word)-2)+word[-1])
    else:
        print(word)
