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

operation_symbol = input("Pick another operation: ")
num3 = int(input("what's the next number?: "))
calculation_function = operations[operation_symbol] 
second_answer = calculation_function(answer, num3)

print(f"{answer} {operation_symbol} {num3} = {second_answer}")