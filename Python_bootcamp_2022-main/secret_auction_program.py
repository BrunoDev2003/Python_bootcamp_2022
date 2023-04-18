from replit import clear
from art.py import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
name = {}
bid = {}
bidding_done = False
option = str
print("welcome to the secret auction program")
while not bidding_done:
  name = input("What is your name?")
  price = input("what is your bid? $$")
  bid[name] = price

  option = input("are the other users who want to bid? type yes or no.")

  if option == "no":
    bidding_done = True

  elif option == "yes":
    bidding_done = True
    clear()