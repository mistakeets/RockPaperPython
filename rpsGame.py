print("Made by Keith Oppel. Visit https://github.com/mistakeets)
youLose = ("The computer wins")
win = ("You win")
lives = 5
score = 0
draw = 0
computer_lives = 7

while True: 
  print("To begin fill in the below information")
  username = input("Please enter your username: ")
  password = input("please enter your password: ")
  searchfile = open("accounts.csv", "r")
  for line in searchfile:
    if username and password in line: 
      print("Access Granted")
      print("Rock Paper Scissors")
      print("Rules of the Game")
      print("You Start with", lives, "lives")
      print("If you win, you get an extra life")
      print("If you lose, you lose a life")
      print("If the round is a draw, your life count stays the same")
      print("------------------------------------------------------")
      print("PLEASE DO NOT USE CAPTIAL LETTERS FOR THE COMMANDS")
      print("------------------------------------------------------")
      print("To see a list of rules, type rules")
      print("At any point type exit to leave the game")
      print("------------------------------------------------------")
      print("The computer also has lives")
      print("Can you beat the computer?")
      print("Good Luck!")
      print("------------------------------------------------------")
