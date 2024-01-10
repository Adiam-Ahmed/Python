import os

def clear():
   os.system('cls' if os.name == 'nt' else 'clear')

from art import logo
print(logo)

bid_score = {}
names = input("what is your name ?: ")
bids = int(input("What's your bid ?:$"))
go_again = input("Are there any other bidders ? Type yes or no. ").lower()


def bid_fun(names,bids,go_again):
  
  bid_score[names] = bids
  if go_again=="yes":
    clear()
    names = input("what is your name ?: ")
    bids = int(input("What's your bid ?:$"))
    go_again = input("Are there any other bidders ? Type yes or no. ").lower()
    bid_fun(names,bids,go_again)

  elif go_again=="no":
    max_value = 0
    max_key = ""
    for key, value in bid_score.items():
      if value > max_value:
        max_value = value
        max_key = key
    print(f"The winner is {max_key} with a bid of ${value}")
  
     
  

bid_fun(names,bids,go_again)


 
#HINT: You can call clear() to clear the output in the console.