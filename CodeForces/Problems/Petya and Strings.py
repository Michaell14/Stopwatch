

#alpha=["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alpha="abcdefghijklmnopqrstuvwxyz"
str1=input().lower()
str2=input().lower()
things=0
words=[[x,y] for (x,y) in zip(str1, str2) if x!=y]

if (len(words)>0):
    things=int([-(alpha.index(y)-alpha.index(x)) for (x,y) in words][0])

if (things<0):
    print(-1)
elif (things>0):
    print(1)
else:
    print(0)
