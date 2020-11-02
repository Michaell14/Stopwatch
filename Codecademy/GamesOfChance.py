import random

money = 100
#Write your game of chance functions here

def coin_flip(bet, choice):
  winner=random.randint(1,2)
  if (winner==1 and choice=="Heads"):
      return bet
  if (winner==2 and choice=="Tails"):
    return bet
  else:
    return -bet

def ChoHan(bet, choice):
  dice1=random.randint(1,6)
  dice2=random.randint(1,6)
  if ((dice1+dice2)%2==0 and choice=="Even"):
    return bet
  elif ((dice1+dice2)%2==1 and choice=="Odd"):
    return bet
  else:
    return -bet

def higher_card(bet, choice):
  nums=list(range(1,14))
  num1=random.randint(1,13)
  nums.remove(num1)
  num2=random.randint(1,13)
  while(num2 not in nums):
    num2=random.randint(1,13)

  if (num1<num2 and choice=="Higher"):
    return bet
  elif (num1>num2 and choice=="Lower"):
    return bet
  else:
    return -bet

def roulette(bet, choice):
  nums=[0,00]
  nums+=list(range(40))
  fromlist=random.randint(0,len(nums))
  if (nums[fromlist]==0 or nums[fromlist]==00):
    return -bet
  elif (str(nums[fromlist])==choice):
    return bet*5
  elif (nums[fromlist]%2==0 and choice=="Even"):
    return bet
  elif (nums[fromlist]%2==1 and choice=="Odd"):
    return bet
  else:
    return -bet

#Call your game of chance functions here
choice=1
while(choice!=5):
  print("Money: ", money)
  print("Choices: ")
  print("1) Coin Flip")
  print("2) Roulette")
  print("3) Cho Han")
  print("4) Higher or Lower")
  print("5) Exit")
  choice=int(input("Enter your choice: "))
  if (choice==5):
    break
  bet=int(input("Enter your bet: "))
  if (choice==1):
    choice=input("Would you like to bet (Heads) or (Tails)?: ")
    change=coin_flip(bet, choice)
    money+=change
  elif(choice==2):
    print("Would you like to bet (Even) or (Odd)?: ")
    print("You may even select a specific number for a chance for 5x the reward. (0-40)")
    choice=input("Choice: ")
    change=roulette(bet, choice)
    money+=change
  elif (choice==3):
    choice=input("Would you like to bet (Even) or (Odd)?: ")
    change=ChoHan(bet, choice)
    money+=change
  elif (choice==4):
    choice=input("Would you like to bet (Higher) or (Lower)?: ")
    change=higher_card(bet, choice)
    money+=change
  
  if (change>0):
    print("You won $", change,"!")
  elif (change<0):
    print("You lost $", -change, "  :(")








