print("-----------------------------------")
print("Rock, Paper, Scissors Account Setup")
print("-----------------------------------")
while True:
  username = input("Pick a username: ")
  password = input("Pick a password: ")
  password_confirm = input("Please confirm password: ")

  if password != password_confirm:
    print("Your password does not match. Please try again")

  if password == password_confirm:
    print("Your account has been created.")
    text_file = open("accounts.txt","a")
    text_file.write("\n")
    text_file.write(username)
    text_file.write("\n")
    text_file.write(password)
    text_file.close()
    break
