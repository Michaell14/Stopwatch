#my own little story
def whatIsName():
    print("What is your name?")
    name=input()
    print("hmm...",name)
    print("Is that correct? (Yes/No)")
    answer=input()
    while(answer=="No"):
        print("What is your name?")
        name=input()
        print("hmm...",name)
        print("Is that correct? (Yes/No)")
        answer=input()
    return name

names=["bob", "joe", "sam", "rob"]
print("Welcome to your very own text story!")
whatIsName()
print(name,", Fantastic! Yes... very cool")
print("Well hello ", name, ". This is the start of your text story.")
