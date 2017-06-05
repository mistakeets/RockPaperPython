print("Made by Keith Oppel. Visit https://github.com/mistakeets)
youLose = ("The computer wins")
win = ("You win")
lives = 5
score = 0
tieGame = 0
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
      while True:
        rps = input("Rock, Paper, Scissors?")
        import random
        computer = ("rock", "paper", "scissors")
        computer = random.choice(computer)
        #rock if statements
        if rps == "rock" and computer == "paper":
          print("The computer chose", computer)
          print("")
          print(youLose)
          print("")
          print("")
          lives-=1 
        if rps == "rock" and computer == "scissors":
          print("The computer chose", computer)
          print("")
          print(win)
          print("")
          print("")
          score+=1
        #paper if statements
        if rps == "paper" and computer == "rock":
          print("The computer chose", computer)
          print("")
          print(win)
          computer_lives -= 1
          print("")
          print("")
          score+=1
        if rps == "paper" and computer == "scissors":
          print("The computer chose", computer)
          print("")
          print(youLose)
          print("")
          print("")
          lives-=1
        #scissors if statements
        if rps == "scissors" and computer == "paper":
          print("The computer chose", computer)
          print("")
          print(win)
          computer_lives-=1
          print("")
          print("")
          score+=1 
        if rps == "scissors" and computer == "rock":
          print("The computer chose", computer)
          print("")
          print(youLose)
          print("")
          print("")
          lives-=1
        #duplicates
        if rps == "rock" and computer == "rock":
          print("The computer chose", computer)
          print("")
          print("It's a draw!")
          print("")
          print("")
          tieGame+=1
        if rps == "paper" and computer == "paper":
          print("The computer chose", computer)
          print("")
          print("It's a draw!")
          print("")
          print("")
          tieGame+=1
        if rps == "scissors" and computer == "scissors":
          print("The computer chose", computer)
          print("")
          print("It's a draw!")
          print("")
          print("")
          tieGame+=1
        #system
        if rps == "rules":
          print("**************************************")
          print("The Rules")
          print("**************************************")
          print("Paper beats Rock")
          print("Rock beats Scissors")
          print("Scissors beats Paper")
          print("**************************************")
        if rps == "display lives":
          print(live)
        if rps == "display score":
          print(score)
        if rps == "display tie games":
          print(tieGame)
        #lives
        if lives == 0 or rps == "test":
          print("Thanks for playing")
          print("You have run out of lives")
          print("You got",score, "correct")
          print("There were", tieGame, "Tie Games")
          stop = input("Press enter key to exit.")
          import time
          time.sleep(900)
        if computer_lives == 0:
          print("Thanks for playing")
          print("The computer has run out of lives")
          print("You win!")
          print("You got",score, "correct")
          print("There were", tieGame, "Tie Games")
          stop = input("Press enter key to exit.")
          import time
          time.sleep(900)
        #exit
        if rps == "exit":
          break



