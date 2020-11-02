s=input()
t=True
for i in range(10):
    if (str(i) in s):
        if (s.count("4") +s.count("7")== 7 or s.count("4") +s.count("7")== 4):
            print("YES")
            t=False
            
            break
if t:
    print("NO")

            
