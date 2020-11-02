alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
comet=input()
group=input()

cometS=1
groupS=1
for i in group:
    groupS*=alpha.find(i)+1
for i in comet:
    cometS*=alpha.find(i)+1
    
if (cometS%47==groupS%47):
    print("GO")
else:
    print("STAY")
