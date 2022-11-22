from art import logo

list = [1,2,3,4,5,6,7,8,9,10]

def start_game():
  print(logo)
  print('Welcome to the Number Guessing Game!')
  print('I1m thinking of a number between 1 and 10')
  dificulty = input(print("choose dificulty"))
  if dificulty == 'hard':
    print("You have 5 attempts remaining to guess a number.")
    while number in list