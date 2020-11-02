alphabet=["a","b", "c", "d", "e", "f", "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(alphabet)
cipherText=[]
text="michael"
cipher=""
for i in text:
    if (i!=" " and not i in cipherText):
        cipherText.append(i)
for x in alphabet:
    if (not x in cipherText):
        cipherText.append(x)
print(cipherText)

hiddenText="ryan"

for i in range(0, len(hiddenText)):
    for x in range(0, len(alphabet)):
        if (alphabet[x]==hiddenText[i]):
            cipher+=cipherText[x]

print(cipher)
