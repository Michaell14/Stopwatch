import os

print(os.getcwd())
os.chdir("/Users/Jianke/Documents/Michael")
#os.makedirs("DeleteFolderLater")
#os.rmdir("lol")
print(os.listdir())

os.rename("DeleteFolderLater", "lol")
print(os.listdir())
print(os.stat("lol"))
print(os.)