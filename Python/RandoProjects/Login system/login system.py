import os


def create_account(f):

    for pair in f:
        user=pair.split(":")[0]
        if (user==username):
            print("That username is taken")
            return False
    return True

def add_to_file(username, password, f):
    f.write("\n%s:%s" %(username, password))

def login(username, password):
    
 

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

print("Welcome to the login system.")
print("Would you like to: \n1)login\n2)Create Account")
choice=int(input())

#They want to LOGIN
if (choice==1):
    username=input("Enter your username: ")
    password=input("Enter your password: ")

#They want to REGISTER ACCOUNT
elif (choice==2):
    username=input("Enter your username: ")
    password1=input("Enter your password: ")
    password2=input("Confirm your password: ")

    
    f=open("database.txt", "r")
    working=create_account(f)
    f.close()

    
    if working:
        if (password1==password2):
            f=open("database.txt", "a")
            add_to_file(username, password1, f)
            f.close()
            print("Created")
        else:
            print("Passwords don't match")
    
