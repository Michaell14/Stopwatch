#Multiplicative

print("Would you like to decrypt or encrypt a word/phrase? (d/e)")
answer=input()
if (answer=="d" or answer=="decrypt"):
    decrypt()
elif (answer=="e" or answer="encrypt"):
    encrypt()
else:
    print("Invalid answer")

def encrpyt():
    alphabet=["a","b", "c", "d", "e", "f", "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    word=input("Enter the word to encrypt:")
    m=int(input("Enter 'M':"))
    a=int(input("Enter 'A':"))
    cipher=""

    for x in word:
        if (x==" "):
            cipher+=" "
        for i in range(0,len(alphabet)):
            if (alphabet[i]==x):
                d=(i*m+a)%26
                cipher+=alphabet[d]
    print(cipher)

def decrypt():
    alphabet=["a","b", "c", "d", "e", "f", "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    word=input("Enter the word to encrypt:")
    m=int(input("Enter 'M':"))
    a=int(input("Enter 'A':"))
    cipher=""

    for x in word:
        if (x==" "):
            cipher+=" "
        for i in range(0, len(alphabet)):
            if (x==alphabet[i]):
                c=((i-a)*9)%26
                cipher+=alphabet[c]
    print(cipher)
decrypt()
