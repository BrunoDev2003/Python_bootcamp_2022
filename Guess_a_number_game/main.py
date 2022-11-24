from art import logo
import random
#from replit import clear

list = [1,2,3,4,5,6,7,8,9,10]
number = random.choice(list)


def start_game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 10")
  dificulty = input(print("choose dificulty. Type 'easy' or 'hard': "))
  if dificulty == 'hard':
    print("You have 5 attempts remaining to guess a number.")
    guess = input(print("Make a guess: "))
    if guess > number:
      print("Too high \n Guess again.")
    if guess < number:
      print("Too low \n Guess again.")
      
      