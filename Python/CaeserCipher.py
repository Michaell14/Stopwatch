#Caeser Cipher
#Michael Li

alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
newAlphabet=[]
print(alphabet)

#Asks for shift direction
print("Shift to left or right? (l/r)")
direction=input()
direction.lower()

p=-1
if (direction=="l" or direction=="left"):
    p=1

#Asks for number of units to shift
print("How many units would you like to shift it?")
units=input()

#Shifts alphabet
for i in range(0, len(alphabet)):
    newAlphabet.append(alphabet[(i-(int(units)*p)%26)])
print(newAlphabet)

#encrypts a word from the user
print("Enter the word you want to be encrypted:")
word=input()


cipher=""

#Encrypts word
for x in word:
    if (x==" "):
        cipher+=" "
    for i in range(0, len(alphabet)):
        if (x==alphabet[i]):
            cipher+=newAlphabet[i]

print(cipher)

