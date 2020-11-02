#with open("openTutorial/openTutorial.txt", 'r') as f:
#    sizeToRead=10
#    contents=f.read(sizeToRead)

#    while (len(contents)>0):
#        print(contents, end="")
#        contents=f.read(sizeToRead)
 
with open("openTutorial/openTutorial2.txt", "r") as f:
    with open("openTutorial/openTutorial3.txt", "w") as ff:
        for i in f:
            ff.write(i)