for i in range(int(input())):
    n=int(input())
    lst=[int(x) for x in input().split(" ")]
    lst2=sorted(lst, reverse=True)
    if lst==lst2 and len(lst)==len(set(lst2)):
        print("NO")
    else:
        print("YES")
    
