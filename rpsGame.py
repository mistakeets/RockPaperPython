import time
print("Made by Keith Oppel. Visit https://github.com/mistakeets")
youLose = ("The computer wins")
win = ("You win")
lives = 5
score = 0
tieGame = 0
computer_lives = 7
password_list = []
while True: 
  print("To begin fill in the below information")
  username = input("Please enter your username: ")
  password = input("please enter your password: ")
  searchfile = open("accounts.txt", "r")
  for line in searchfile:
    password_list.append(line.strip())
    if username and password in password_list:
      print("Access Granted")
      time.sleep(0.5)
      print("Loading..")
      time.sleep(0.5)
      print("Loading..")
      time.sleep(0.5)
      print("Loading..")
      time.sleep(0.5)
      start_menu = """
      Rock Paper Scissors
      Rules of the Game
      You Start with 5 lives
      If you win, you get an extra life
      If you lose, you lose a life
      If the round is a draw, your life count stays the same
      ------------------------------------------------------
      To see a list of rules, type rules
      At any point type exit to leave the game
      ------------------------------------------------------
      The computer also has lives
      Can you beat the computer?
      Good Luck!
      ------------------------------------------------------
      """
      while True:
        rps = input("Rock, Paper, Scissors?   ")
        rps = rps.title()
        import random
        computer = ("rock", "paper", "scissors")
        computer = random.choice(computer)
        #rock if statements
        if rps == "Rock" and computer == "paper":
          print("The computer chose", computer)
          print("")
          print(youLose)
          print("")
          print("")
          lives-=1 
        if rps == "Rock" and computer == "scissors":
          print("The computer chose", computer)
          print("")
          print(win)
          print("")
          print("")
          score+=1
        #paper if statements
        if rps == "Paper" and computer == "rock":
          print("The computer chose", computer)
          print("")
          print(win)
          computer_lives -= 1
          print("")
          print("")
          score+=1
        if rps == "Paper" and computer == "scissors":
          print("The computer chose", computer)
          print("")
          print(youLose)
          print("")
          print("")
          lives-=1
        #scissors if statements
        if rps == "Scissors" and computer == "paper":
          print("The computer chose", computer)
          print("")
          print(win)
          computer_lives-=1
          print("")
          print("")
          score+=1 
        if rps == "Scissors" and computer == "rock":
          print("The computer chose", computer)
          print("")
          print(youLose)
          print("")
          print("")
          lives-=1
        #duplicates
        if rps == "Rock" and computer == "rock":
          print("The computer chose", computer)
          print("")
          print("It's a draw!")
          print("")
          print("")
          tieGame+=1
        if rps == "Paper" and computer == "paper":
          print("The computer chose", computer)
          print("")
          print("It's a draw!")
          print("")
          print("")
          tieGame+=1
        if rps == "Scissors" and computer == "scissors":
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
          exit()
        if computer_lives == 0:
          print("Thanks for playing")
          print("The computer has run out of lives")
          print("You win!")
          print("You got",score, "correct")
          print("There were", tieGame, "Tie Games")
          stop = input("Press enter key to exit.")
          exit()
        #exit
        if rps == "exit":
          break
    else: 
      print("Your username or password is incorrect")
      print("--------------------------------------")



