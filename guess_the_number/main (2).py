from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100")
selected_Num = random.randint(1,101)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

chances = 0

if difficulty == "easy":
  chances = 10
  print(f"You have {chances} attempts remaining to guess the number.")
if difficulty == "hard":
  chances = 5
  print(f"You have {chances} attempts remaining to guess the number.")

guess_Num = int(input("Make a guess: "))


def check_guess(guess_Num):
  global chances
  if guess_Num < selected_Num:
    print("Too Low")
    print("Guess Again")
    chances -= 1
  if guess_Num > selected_Num:
    print("Too high")
    print("Guess Again")
  print(f"You have {chances} attempts remaining to guess the number.")
    
check_guess(guess_Num)

while guess_Num != selected_Num and chances > 0:
  guess_Num = int(input("Make a guess: "))
  check_guess(guess_Num)

if guess_Num == selected_Num:
  print(f"You got it! The answer was {selected_Num}")

if chances == 0:
  print("You lose")




