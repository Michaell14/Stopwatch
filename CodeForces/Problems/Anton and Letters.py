s=input()
lst=[]
for i in s:
    if i != "{" and i!="," and i != "}" and i!=" ":
        lst.append(i)

print(len(set(lst)))
