input()
lst=list(map(int, input().split(" ")))

lst1=list(set(lst))
if 0 in lst1:
    lst1.remove(0)
print(len(lst1))
