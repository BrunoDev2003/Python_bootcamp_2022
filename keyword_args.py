# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("hello")
  print("i'm bruno")
  print("how are you?")

greet()


def greet_with_name(name):
  print("hello")
  print(f"i'm {name}")

greet_with_name("Bruno")

#functions with more then 1 input
def greet_with(name, location):
  print(F"Hello {name}")
  print(F"What is it like in {location}")

#functions with keywords arguments
greet_with(location="London", name="Bruno")