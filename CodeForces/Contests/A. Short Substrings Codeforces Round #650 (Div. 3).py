case=int(input())
i=0
for x in range(case):
    s=input()
    new=s[0]
    for i in range(1, len(s),2):
        new+=s[i]
    print(new)
