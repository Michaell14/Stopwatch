# AP CSP
# Hangman
import sys
import random

lives = 0
correct = 0
Answer = ["_", "_", "_"]
Easy = ["cat", "dog", "ate", "man", "old"]
Intermediate = ["Oxygen", "Zombie", "absent", "baboon", "cabins"]
Hard = ["accelerators", "camouflaging", "Pennsylvania", "Philadelphia", "maidservants"]


def menu():
  print("===================================================================")
  print("\t\tHangman")
  print("1 - Information")
  print("2 - Easy mode")
  print("3 - Intermediate mode")
  print("4 - Hard mode")
  print("5 - Give-up")
  print("===================================================================")
  main()


def infor():
  print("Welcome to Hangman!")
  print("There are three levels you can try: Easy, Medium or Hard.")
  print("You have 8 lives for Easy, 7 lives for Medium, and 6 lives for Hard.")
  print("In all modes, you can get a 5/5 correct, you get a perfect score!")
  print("Another option is you can just give-up and not play with this game.")
  print("REMEMBER, IF YOU TYPE GIVE-UP, YOU CORRECT SCORE WILL RESET TO ZERO ALWAYS. THE WHOLE POINT IS TO WIN!")
  print("Enjoy and have fun!")


def easylives(lives):
  if (lives == 8):
      print("  _______   ")
      print("  |     o   ")
      print("  |    <|>  ")
      print("  |    / \  ")
      print(" ---  ~   ~ ")
  elif (lives == 7):
      print("  _______   ")
      print("  |     o   ")
      print("  |    <|>  ")
      print("  |    / \  ")
      print(" ---  ~     ")
  elif (lives == 6):
      print("  _______   ")
      print("  |     o   ")
      print("  |    <|>  ")
      print("  |    / \  ")
      print(" ---        ")
  elif (lives == 5):
      print("  _______   ")
      print("  |     o   ")
      print("  |    <|>  ")
      print("  |    /    ")
      print(" ---        ")
  elif (lives == 4):
      print("  _______   ")
      print("  |     o   ")
      print("  |    <|>  ")
      print("  |         ")
      print(" ---        ")
  elif (lives == 3):
      print("  _______   ")
      print("  |     o   ")
      print("  |    <|   ")
      print("  |         ")
      print(" ---        ")
  elif (lives == 2):
      print("  _______   ")
      print("  |     o   ")
      print("  |     |   ")
      print("  |         ")
      print(" ---        ")
  elif (lives == 1):
      print("  _______   ")
      print("  |     o   ")
      print("  |         ")
      print("  |         ")
      print(" ---        ")
  return lives

#Child algorithm
def easy(correct, Answer):
   lives = 8
   while (correct < 5):
      words = random.choice(Easy)
      while (lives > 0):
          easylives(lives)
          print("You currently have", lives, "lives.")
          print(Answer)
          print("\n")
          guess = raw_input("Guess a letter or the word: ")
          if (guess != words) and (guess not in words):
              lives -= 1
              print("That is not a letter in the word.")
              continue
          if (guess in words) and (len(guess) == 1):
              if (guess in Answer):
                  print("The character already exists.")
                  continue
              print("Congrats! That is in the word.")
              NewAnswer = []
              for xx in range(len(Answer)):
                  if (xx == words.index(guess)):
                      NewAnswer.append(guess)
                  elif (Answer[xx] != "_"):
                      NewAnswer.append(Answer[xx])
                  else:
                      NewAnswer.append("_")
              Answer = NewAnswer
              Temp = ""
              for x in Answer:
                  Temp += x
              if (Temp == words):
                  correct += 1
                  print("You got", correct, "correct. Good Job!")
                  Answer = ["_", "_", "_"]
                  print("\n")
                  print("New word is assigned!")
                  break
              continue
          if (guess == words):
              correct += 1
              print("You got", correct, "correct. Good Job!")
              Answer = ["_", "_", "_"]
              print("\n")
              print("New word is assigned!")
          if (correct == 5):
              break;
      if (correct == 5):
          win()
          main()
      if lives == 0:
          game_Over(correct)
          main()



def inter():
  lives = 7
  if (lives == 7):
      print("  _______   ")
      print("  |     _   ")
      print("  |     o   ")
      print("  |    <|>  ")
      print("  |    / \  ")
      print(" ---        ")
  elif (lives == 6):
      print("  _______   ")
      print("  |     _   ")
      print("  |     o   ")
      print("  |    <|>  ")
      print("  |    /    ")
      print(" ---        ")
  elif (lives == 5):
      print("  _______   ")
      print("  |     _   ")
      print("  |     o   ")
      print("  |    <|>  ")
      print("  |         ")
      print(" ---        ")
  elif (lives == 4):
      print("  _______   ")
      print("  |     _   ")
      print("  |     o   ")
      print("  |    <|   ")
      print("  |         ")
      print(" ---        ")
  elif (lives == 3):
      print("  _______   ")
      print("  |     _   ")
      print("  |     o   ")
      print("  |    <    ")
      print("  |         ")
      print(" ---        ")
  elif (lives == 2):
      print("  _______   ")
      print("  |     _   ")
      print("  |     o   ")
      print("  |         ")
      print("  |         ")
      print(" ---        ")
  elif (lives == 1):
      print("  _______   ")
      print("  |     _   ")
      print("  |         ")
      print("  |         ")
      print("  |         ")
      print(" ---        ")
  print("You currently have", lives, "lives.")


def hard():
  lives = 6
  if (lives == 6):
      print("  _______   ")
      print("  |     o   ")
      print("  |    <|>  ")
      print("  |    / \  ")
      print(" ---        ")
  elif (lives == 5):
      print("  _______   ")
      print("  |     o   ")
      print("  |    <|>  ")
      print("  |    /    ")
      print(" ---        ")
  elif (lives == 4):
      print("  _______   ")
      print("  |     o   ")
      print("  |    <|>  ")
      print("  |         ")
      print(" ---        ")
  elif (lives == 3):
      print("  _______   ")
      print("  |     o   ")
      print("  |    <|  ")
      print("  |         ")
      print(" ---        ")
  elif (lives == 2):
      print("  _______   ")
      print("  |     o   ")
      print("  |    <    ")
      print("  |         ")
      print(" ---        ")
  elif (lives == 1):
      print("  _______   ")
      print("  |     o   ")
      print("  |         ")
      print("  |         ")
      print(" ---        ")
  print("You currently have", lives, "lives.")

#Child algorithm and abstraction
def give_Up(correct):
  give_Up = raw_input("Do you want to end the game? (y or n): ")
  while (give_Up != "y") and (give_Up != "n"):
      print("Input is not valid!")
      give_Up = raw_input("Do you want to end the game? (y or n): ")
      if (give_Up == "y") or (give_Up == "n"):
          break;
  if (give_Up == "y"):
      print("Amazing! Try again next time.")
      print("You had", correct, "correct!")
      sys.exit()
  elif (give_Up == "n"):
      menu()
      main()


def game_Over(correct):
  print("You had", correct ,"correct.")
  print("GAME OVER!")

def win():
  if (correct == 5):
      print("You Win!")

#Parent algorithm
def main():
  choice = 0
  while (choice != 5):
      print("\n")
      choice = int(input("Menu Option: "))
      print(" ")
      if (choice == 1):
          infor()
      elif (choice == 2):
          easy(correct, Answer)
      elif (choice == 3):
          inter()
      elif (choice == 4):
          hard()
      elif (choice == 5):
          give_Up(correct)


menu()

