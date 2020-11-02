for i in range(100):
    x=str(i*i)
    if len(x)==4:
        if x[0]==x[1] and x[2]==x[3]:
            print(i)
            print(x)
            break
