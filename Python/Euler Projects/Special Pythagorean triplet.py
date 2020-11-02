def hi():
    for a in range(3,900):
        for b in range(3,900):
            for c in range(333, 998):
                if a+b+c==1000:
                    if a*a+b*b==c*c:
                        print(a)
                        print(b)
                        print(c)
                        return a*b*c
    return 0
print(hi())
