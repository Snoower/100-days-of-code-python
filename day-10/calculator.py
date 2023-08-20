import art
import replit

#Addition
def add(n1, n2):
  return n1 + n2
  
#Subtraction
def subtract(n1, n2):
  return n1 - n2
  
#Multiplication
def multiply(n1, n2):
  return n1 * n2
  
#Division
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(art.logo)
  
  first_number = float(input("What is the first number?: "))
  for symbol in operations:
    print(symbol)
    continue_calculation = True 
    
  while continue_calculation == True:
    operation_symbol = input("Pick an operation: ")
    second_number = float(input("What is the next number?: "))
    calculation_function = operations[operation_symbol]
    result = calculation_function(first_number, second_number)
        
    print(f"{first_number} {operation_symbol} {second_number} = {result}")
    
    decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if decision == "y":
      first_number = result 
    else: 
      continue_calculation = False
      replit.clear()
      calculator()
          
      
calculator()
