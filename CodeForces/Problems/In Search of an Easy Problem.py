input()
lst=list(map(int, input().split()))
f=True
for i in lst:
    if i==1:
        print("HARD")
        f=False
        break
if (f):
    print("EASY")
