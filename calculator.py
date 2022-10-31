from art import logo

print(logo)

def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide

}

num1 = int(input("Whats the first number?: "))
num2 = int(input("Whats the second number?: "))


for symbols in operations:
  print(symbols)

operations_symbols = input("Pick an operation from the line above: ")

calculation_function = operations[operations_symbols]
answer = calculation_function(num1,num2)

print(f"{num1} {operations_symbols} {num2} = {answer}")