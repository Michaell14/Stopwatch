case=int(input())
for i in range(case):
    input()
    lst=list(map(int, input().split(" ")))
    one=lst.count(1)
    zero=lst.count(0)
    f=0
    if one<=zero:
       f=1
    else:
        f=0
    for x in range(min(one, zero)):
        lst.remove(f)

    if 0 not in lst and len(lst)%2==1:
        lst.remove(1)
    print(len(lst))
    print(*lst)
