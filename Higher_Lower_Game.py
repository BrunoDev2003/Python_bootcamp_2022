from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  """Format the account data into printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def compare_followers(guess, account_a, account_b):
  """Take the user guess and follower counts and returns if they got it right"""
  if account_a > account_b:
    return guess == "a"
  else:
    return guess == "b"

#Display art.

print(logo)
score = 0
game_continue = True
account_B = random.choice(data)

#Make the game repeatable.
while game_continue:
  
  #Generate a random account from the game data.

  #Making account at position B become the next account at position A.
  account_A = account_B
  account_B = random.choice(data)
  
  account_A = random.choice(data)
  account_B = random.choice(data)
  
  while account_A == account_B:
    account_B = random.choice(data)
  
  #Format the account data into printable format.
    
  print(f"Compare A: {format_data(account_A)}")
  print(vs)
  print(f"Against B: {format_data(account_B)}")
  
  #Use randint() to generate a random integer.
  
  #Ask user for a guess.
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  #Check if user is correct.
  ##Get Follower count of each account.
  a_follower_count = account_A["follower_count"]
  b_follower_count = account_B["follower_count"]
  
  is_correct = compare_followers(guess, a_follower_count, b_follower_count)

  #Clear the screen between rounds.
  clear()
  print(logo)
  
  ##Use if statement to check if user is correct.
  
  #Give user feedback on their guess.
  if is_correct:
    score += 1
    print(f"Correct! Current score: {score}")
  else:
    game_continue = False
    print(f"Sorry, that's wrong! Final score: {score}")