import art
import random
from game_data import data
import os


lives = 1 
option_A = random.randint(0,len(data)-1)
message_A = f"Compare A: {data[option_A]['name']}, a {data[option_A]['description']}, from {data[option_A]['country']}."
wonLastRound = False
current_scores=0

def checkAnswer(answer, option_B, A, B):
  global wonLastRound
  global message_A
  global current_scores
  global lives

  if answer == 'A' and A > B:
    wonLastRound = True
    current_scores+=1
    message_A = f"Compare A: {data[option_B]['name']}, a {data[option_B]['description']}, from {data[option_B]['country']}."
    os.system('cls')
  elif answer == 'B' and B > A:
    wonLastRound = True
    current_scores+=1
    message_A = f"Compare A: {data[option_B]['name']}, a {data[option_B]['description']}, from {data[option_B]['country']}."
    os.system('cls')
  else:
    os.system('cls')
    lives = 0
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {current_scores}")

while lives == 1:
  option_B = random.randint(0,len(data)-1)

  A = data[option_A]['follower_count']
  B = data[option_B]['follower_count']

  message_B = f"Against B: {data[option_B]['name']}, a {data[option_B]['description']}, from {data[option_B]['country']}."


  print(art.logo)
  if wonLastRound:
    print(f"You're right! Current score: {current_scores}.")     
  print(message_A)
  

  print(art.vs)
  print(message_B)
 
  answer = input("Who has more followers? Type 'A' or 'B':").upper()

  checkAnswer(answer, option_B, A, B)



  
    
    
  



