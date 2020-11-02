#Vigenere Cipher

alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
key=input("Enter keyword: ")
text=input("Enter plaintext: ")
newAlphabet=[]
while len(newAlphabet) <=len(text):  
    for i in key:
        newAlphabet.append(i)
print(newAlphabet)

