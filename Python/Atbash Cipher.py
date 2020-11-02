#Atbash cipher
#Working

alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lengthWords=[]
print("Enter the word/phrase you want to encrypt: ")
word=input()

cipher=""
for x in word:
    if (x==" "):
        cipher+=" "
    for i in range(0, len(alphabet)): 
        if (x==alphabet[i]):
            cipher+=alphabet[(i+1)*-1]
print(cipher)
