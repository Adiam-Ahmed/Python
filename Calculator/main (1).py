import time
import os
from art import logo

os.system('clear')

def clear(seconds = 0):
 time.sleep(seconds)
 os.system('clear')

def add(n1,n2):
  """adds n1 and n2"""
  return n1+n2
def subtract(n1,n2):
  """subtract n1 and n2"""
  return n1-n2
def multiply(n1,n2):
  """multiply n1 and n2"""
  return n1*n2
def divide(n1,n2):
  """divide n1 and n2"""
  return n1/n2
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
             }
def calculator():
  print(logo)
  
  num1 = int(input("What is the first number? "))
  
  for symbol in operations:
    print(symbol)
  operations_symbol= input("Pick an opertions from the line above: ")
  caluculation_fun = operations[operations_symbol]
  num2 = int(input("What is the second number? "))
  
  first_answer = caluculation_fun (num1,num2)
  
  print(f"{num1} {operations_symbol} {num2} = {first_answer}")
  
  continue_cal = input(f"Type y to continue calculating with {first_answer} or type n to exit.: " )
  
  while continue_cal == "y":
    new_operations_symbol= input("Pick an opertions from the line above: ")
    num3 = int(input("What is the next number? "))
    caluculation_fun_1 = operations[new_operations_symbol]
    second_answer = caluculation_fun_1 (caluculation_fun(num1,num2),num3)
    print(f"{first_answer} {new_operations_symbol} {num3} = {second_answer}")
    continue_cal = input(f"Type y to continue calculating with {first_answer} or type n to exit.:" )
    if continue_cal == "n":
      print("clear screen in 3 sec")
      clear(3)
      calculator()
      
calculator()





    