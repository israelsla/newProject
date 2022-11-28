



def welcome(name):
    Your_Name = input("please enter your name <<<<>>>> ")
    print(f'Hello {Your_Name.capitalize()} and welcome to the World of Games (WoG). Here you can find many cool games to play')


def load_game():
   print("You have a three game that you can play <><> ")
   print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back ")
   print("2. Guess Game - guess a number and see if you chose like the computer ")
   print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS ")
   Your_choose = int(input("Please choose a game that you want to play between 1-3: "))
   while Your_choose > 3 or Your_choose <= 0:
       print("Error, you need to choose number between 1-3 ")
       Your_choose = int(input("Please choose a game that you want to play between 1-3: "))

   Difficulty = int(input("which diffculty you want to play? between 1 - 5 "))
   while Difficulty > 5 or Difficulty <= 0:
       print("Error, you need number dificult between 1-5 ")
       Difficulty = int(input("which diffculty you want to play? between 1 - 5 "))
   print("Great!!! we started soon ")
   return Difficulty, Your_choose




