from art import logo
import random
#from replit import clear

list = [1,2,3,4,5,6,7,8,9,10]
number = random.choice(list)

attempts_hard = 5
attempts_easy = 10
attempts = 0


def start_game(list):
  print(logo)
  print("Welcome to the Number Guessing Game!\n")
  print("I'm thinking of a number between 1 and 10\n")
  dificulty = input(print("choose dificulty. Type 'easy' or 'hard': "))
  if dificulty == 'hard':
    while attempts < 5:   
      print(f"You have {attempts_hard} attempts remaining to guess a number.")
      guess = input(print("Make a guess: "))
      if guess > number:
        attempts + 1
        print("Too high \n Guess again.")
      if guess < number:
        attempts + 1
        print("Too low \n Guess again.")

      elif guess == number:
        print("You got it!")

        
  elif dificulty == 'easy':
    while attempts < 10:   
      print(f"You have {attempts_easy} attempts remaining to guess a number.")
      guess = input(print("Make a guess: "))
      if guess >= number:
        attempts + 1
        print("Too high \n Guess again.")
      if guess <= number:
        attempts + 1
        print("Too low \n Guess again.")

start_game(list)